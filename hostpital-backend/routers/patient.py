# routers/patient.py — Patient panel endpoints
from fastapi import APIRouter, HTTPException, status
from datetime import datetime, timezone

from database import get_db
from models.patient_model import RegisterPatientRequest
from services.scoring import calculate_priority_score, classify_priority
from utils.id_generator import generate_patient_id

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_patient(body: RegisterPatientRequest):
    """
    Register a new patient:
    1. Calculate priority score from symptoms
    2. Classify into Low / Medium / High
    3. Generate unique patient ID
    4. Store in MongoDB
    """
    db = get_db()
    score = calculate_priority_score(body.symptoms)
    level = classify_priority(score)
    pid   = generate_patient_id()

    doc = {
        "patient_id":     pid,
        "name":           body.name,
        "age":            body.age,
        "contact_phone":  body.contact_phone,
        "symptoms":       body.symptoms,
        "symptom_text":   body.symptom_text,
        "priority_score": score,
        "priority_level": level.value,
        "status":         "waiting",
        "bed_id":         None,
        "assigned_nurse_id":  None,
        "assigned_doctor_id": None,
        "surgery_scheduled":  None,
        "llm_insights":   None,
        "doctor_decision": None,
        "created_at":     datetime.now(timezone.utc),
    }

    await db.patients.insert_one(doc)

    return {
        "patient_id":     pid,
        "priority_score": score,
        "priority_level": level.value,
        "message":        "Patient registered successfully",
    }


@router.get("/{patient_id}")
async def get_patient(patient_id: str):
    """Retrieve full patient record by patient_id."""
    db = get_db()
    patient = await db.patients.find_one(
        {"patient_id": patient_id}, {"_id": 0}
    )
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.get("/{patient_id}/status")
async def get_patient_status(patient_id: str):
    """
    Lightweight status check for the Patient Panel:
    queue position, assigned resources, current status.
    """
    db = get_db()
    patient = await db.patients.find_one(
        {"patient_id": patient_id},
        {"_id": 0, "status": 1, "bed_id": 1, "assigned_nurse_id": 1,
         "assigned_doctor_id": 1, "priority_level": 1, "priority_score": 1},
    )
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Calculate queue position (patients ahead with higher or equal priority waiting)
    queue_position = await db.patients.count_documents({
        "status": "waiting",
        "priority_score": {"$gt": patient["priority_score"]},
    })

    return {**patient, "queue_position": queue_position + 1}


@router.get("/{patient_id}/discharge-report")
async def get_discharge_report(patient_id: str):
    """Return the discharge summary for a patient (shown in Patient Panel)."""
    db = get_db()
    report = await db.discharge_summaries.find_one(
        {"patient_id": patient_id}, {"_id": 0}
    )
    if not report:
        raise HTTPException(status_code=404, detail="Discharge report not found")
    return report
