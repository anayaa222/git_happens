# routers/doctor.py — Doctor panel endpoints
from fastapi import APIRouter, HTTPException, Query
from datetime import datetime, timezone

from database import get_db
from models.patient_model import DecisionRequest, AssignRequest
from services.llm_service import analyse_patient

router = APIRouter()


@router.get("/queue")
async def get_patient_queue():
    """
    Full priority-sorted queue for the Doctor dashboard.
    Returns all non-discharged patients, sorted by priority_score descending.
    """
    db = get_db()
    patients = await db.patients.find(
        {"status": {"$ne": "discharged"}},
        {"_id": 0},
        sort=[("priority_score", -1), ("created_at", 1)],
    ).to_list(length=200)
    return {"queue": patients, "count": len(patients)}


@router.get("/patient/{patient_id}/llm-insights")
async def get_llm_insights(patient_id: str, refresh: bool = False):
    """
    Return LLM insights for a patient.
    If insights already exist and refresh=False, returns cached version.
    If refresh=True or no insights exist, calls Gemini API.
    """
    db = get_db()
    patient = await db.patients.find_one({"patient_id": patient_id}, {"_id": 0})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    if patient.get("llm_insights") and not refresh:
        return {"source": "cache", "insights": patient["llm_insights"]}

    # Fetch latest vitals for context
    vitals = await db.vitals.find(
        {"patient_id": patient_id},
        {"_id": 0},
        sort=[("recorded_at", -1)],
        limit=3,
    ).to_list(length=3)

    insights = await analyse_patient(patient, vitals)
    insights["generated_at"] = datetime.now(timezone.utc).isoformat()

    # Cache insights in patient document
    await db.patients.update_one(
        {"patient_id": patient_id},
        {"$set": {"llm_insights": insights}},
    )

    return {"source": "llm", "insights": insights}


@router.post("/patient/{patient_id}/decision")
async def submit_decision(patient_id: str, body: DecisionRequest):
    """
    Doctor approves or rejects LLM suggestion, adds notes and prescription.
    """
    db = get_db()
    patient = await db.patients.find_one({"patient_id": patient_id})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    decision = {
        "approved_llm": body.approved_llm,
        "notes":        body.notes,
        "prescription": body.prescription,
        "decided_at":   datetime.now(timezone.utc),
    }

    await db.patients.update_one(
        {"patient_id": patient_id},
        {"$set": {"doctor_decision": decision}},
    )

    return {"message": "Decision recorded", "decision": decision}


@router.post("/patient/{patient_id}/assign")
async def assign_resources(patient_id: str, body: AssignRequest):
    """
    Assign bed, nurse, doctor, and/or surgery schedule to a patient.
    Automatically updates patient status to 'admitted' if bed is assigned.
    """
    db = get_db()
    patient = await db.patients.find_one({"patient_id": patient_id})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    updates: dict = {}
    if body.bed_id:
        updates["bed_id"]  = body.bed_id
        updates["status"]  = "admitted"
    if body.nurse_id:
        updates["assigned_nurse_id"]  = body.nurse_id
    if body.doctor_id:
        updates["assigned_doctor_id"] = body.doctor_id
    if body.surgery_scheduled:
        updates["surgery_scheduled"] = body.surgery_scheduled
        updates["status"] = "surgery"

    if updates:
        await db.patients.update_one(
            {"patient_id": patient_id},
            {"$set": updates},
        )

    return {"message": "Resources assigned", "updates": updates}


@router.post("/patient/{patient_id}/discharge")
async def discharge_patient(patient_id: str):
    """
    Discharge a patient:
    1. Gather all data (symptoms, vitals, reports, LLM insights, doctor notes)
    2. Write discharge_summary document
    3. Update patient status to 'discharged'
    """
    db = get_db()
    patient = await db.patients.find_one({"patient_id": patient_id}, {"_id": 0})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    if patient.get("status") == "discharged":
        raise HTTPException(status_code=400, detail="Patient already discharged")

    # Fetch vitals history
    vitals_history = await db.vitals.find(
        {"patient_id": patient_id}, {"_id": 0}
    ).to_list(length=None)

    summary_doc = {
        "patient_id":    patient_id,
        "patient_name":  patient.get("name"),
        "age":           patient.get("age"),
        "symptoms":      patient.get("symptoms", []),
        "symptom_text":  patient.get("symptom_text", ""),
        "priority_level": patient.get("priority_level"),
        "vitals_history": vitals_history,
        "reports":        patient.get("reports", []),
        "llm_insights":   patient.get("llm_insights"),
        "doctor_decision": patient.get("doctor_decision"),
        "bed_id":          patient.get("bed_id"),
        "discharged_at":   datetime.now(timezone.utc),
    }

    await db.discharge_summaries.insert_one(summary_doc)
    await db.patients.update_one(
        {"patient_id": patient_id},
        {"$set": {"status": "discharged"}},
    )

    return {"message": "Patient discharged successfully", "patient_id": patient_id}


@router.get("/alerts")
async def get_doctor_alerts(acknowledged: bool = False):
    """Fetch active critical alerts directed at doctors."""
    db = get_db()
    query = {"target_role": "doctor"}
    if not acknowledged:
        query["acknowledged"] = False

    alerts = await db.alerts.find(
        query, {"_id": 0}, sort=[("created_at", -1)]
    ).to_list(length=50)
    return {"alerts": alerts, "count": len(alerts)}
