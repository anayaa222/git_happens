# routers/discharge.py
from fastapi import APIRouter, HTTPException
from database import get_db

router = APIRouter()


@router.get("/{patient_id}")
async def get_discharge_summary(patient_id: str):
    """Return full discharge summary for a patient."""
    db = get_db()
    summary = await db.discharge_summaries.find_one(
        {"patient_id": patient_id}, {"_id": 0}
    )
    if not summary:
        raise HTTPException(status_code=404, detail="Discharge summary not found")
    return summary


@router.get("/")
async def list_discharge_summaries(limit: int = 20):
    """List recent discharge summaries (admin/doctor view)."""
    db = get_db()
    summaries = await db.discharge_summaries.find(
        {},
        {"_id": 0, "patient_id": 1, "patient_name": 1, "discharged_at": 1},
        sort=[("discharged_at", -1)],
    ).to_list(length=limit)
    return {"summaries": summaries}
