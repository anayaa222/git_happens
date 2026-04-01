# routers/nurse.py — Nurse panel endpoints
from fastapi import APIRouter, HTTPException, UploadFile, File, Query
from datetime import datetime, timezone

from database import get_db, get_fs
from models.vitals_model import VitalsRequest
from utils.vitals_rules import check_vitals

router = APIRouter()


@router.get("/assigned-patients")
async def get_assigned_patients(nurse_id: str = Query(..., description="Nurse user ID")):
    """List all patients currently assigned to this nurse."""
    db = get_db()
    patients = await db.patients.find(
        {"assigned_nurse_id": nurse_id, "status": {"$ne": "discharged"}},
        {"_id": 0, "patient_id": 1, "name": 1, "age": 1,
         "priority_level": 1, "status": 1, "bed_id": 1},
    ).to_list(length=100)
    return {"patients": patients, "count": len(patients)}


@router.post("/vitals/{patient_id}")
async def submit_vitals(patient_id: str, body: VitalsRequest):
    """
    Submit a vitals reading for a patient.
    Automatically runs rule-based alert check.
    If an alert is triggered, it is stored in the alerts collection.
    """
    db = get_db()

    # Verify patient exists
    patient = await db.patients.find_one({"patient_id": patient_id})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    vitals_dict = body.model_dump()
    alert_level, alert_message = check_vitals(vitals_dict)

    vitals_doc = {
        "patient_id":        patient_id,
        **vitals_dict,
        "alert_triggered":   alert_level,
        "recorded_at":       datetime.now(timezone.utc),
    }
    await db.vitals.insert_one(vitals_doc)

    # Create alert if thresholds breached
    if alert_level:
        target_role = "doctor" if alert_level == "critical" else "nurse"
        await db.alerts.insert_one({
            "patient_id":   patient_id,
            "type":         alert_level,
            "message":      alert_message,
            "target_role":  target_role,
            "acknowledged": False,
            "created_at":   datetime.now(timezone.utc),
        })

    return {
        "message":       "Vitals recorded",
        "alert_level":   alert_level,
        "alert_message": alert_message,
    }


@router.get("/vitals/{patient_id}")
async def get_vitals_history(patient_id: str, limit: int = 10):
    """Fetch the N most recent vitals for a patient."""
    db = get_db()
    vitals = await db.vitals.find(
        {"patient_id": patient_id},
        {"_id": 0},
        sort=[("recorded_at", -1)],
        limit=limit,
    ).to_list(length=limit)
    return {"vitals": vitals}


@router.post("/upload-report/{patient_id}")
async def upload_report(patient_id: str, file: UploadFile = File(...)):
    """
    Upload a medical report (PDF or image) for a patient.
    Stored in MongoDB GridFS and linked via patient_id.
    """
    db  = get_db()
    fs  = get_fs()

    # Validate patient exists
    patient = await db.patients.find_one({"patient_id": patient_id})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    allowed_types = {"application/pdf", "image/jpeg", "image/png", "image/webp"}
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Only PDF and image files are allowed")

    contents = await file.read()
    file_id = await fs.upload_from_stream(
        filename=file.filename,
        source=contents,
        metadata={
            "patient_id":   patient_id,
            "content_type": file.content_type,
            "uploaded_at":  datetime.now(timezone.utc).isoformat(),
        },
    )

    # Record reference in patient document
    await db.patients.update_one(
        {"patient_id": patient_id},
        {"$push": {"reports": str(file_id)}},
    )

    return {
        "message":   "Report uploaded successfully",
        "file_id":   str(file_id),
        "file_name": file.filename,
    }


@router.get("/alerts")
async def get_nurse_alerts(acknowledged: bool = False):
    """Fetch active (or all) alerts directed at nurses."""
    db = get_db()
    query = {"target_role": "nurse"}
    if not acknowledged:
        query["acknowledged"] = False

    alerts = await db.alerts.find(
        query,
        {"_id": 0},
        sort=[("created_at", -1)],
    ).to_list(length=50)
    return {"alerts": alerts, "count": len(alerts)}


@router.put("/alerts/{alert_id}/acknowledge")
async def acknowledge_alert(alert_id: str):
    """Mark an alert as acknowledged."""
    from bson import ObjectId
    db = get_db()
    result = await db.alerts.update_one(
        {"_id": ObjectId(alert_id)},
        {"$set": {"acknowledged": True}},
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Alert not found")
    return {"message": "Alert acknowledged"}
