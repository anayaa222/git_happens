# routers/queue.py — Queue and bed management
from fastapi import APIRouter, HTTPException
from database import get_db

router = APIRouter()


@router.get("/beds")
async def get_bed_status():
    """Return available vs occupied bed counts."""
    db = get_db()
    occupied = await db.patients.count_documents(
        {"bed_id": {"$ne": None}, "status": {"$ne": "discharged"}}
    )
    # Assuming a fixed capacity — make this configurable in production
    total_beds = 50
    return {
        "total":     total_beds,
        "occupied":  occupied,
        "available": total_beds - occupied,
    }


@router.post("/trigger-llm/{patient_id}")
async def trigger_llm(patient_id: str):
    """Manually trigger LLM analysis for a patient (forces refresh)."""
    from routers.doctor import get_llm_insights
    return await get_llm_insights(patient_id, refresh=True)


@router.put("/reprioritise")
async def reprioritise_queue():
    """
    Re-sort is implicit in MongoDB queries (sorted by priority_score DESC).
    This endpoint exists to allow manual re-triggers or future re-scoring logic.
    """
    return {"message": "Queue is dynamically sorted — no action needed"}


# routers/alerts.py — Generic alert endpoints
from fastapi import APIRouter
from database import get_db
from bson import ObjectId

alerts_router = APIRouter()


@alerts_router.get("/")
async def get_all_alerts(role: str = None, acknowledged: bool = False):
    """Get alerts, optionally filtered by role (nurse/doctor)."""
    db = get_db()
    query = {"acknowledged": acknowledged}
    if role:
        query["target_role"] = role
    alerts = await db.alerts.find(
        query, {"_id": 0}, sort=[("created_at", -1)]
    ).to_list(length=100)
    return {"alerts": alerts}


@alerts_router.put("/{alert_id}/acknowledge")
async def acknowledge(alert_id: str):
    db = get_db()
    result = await db.alerts.update_one(
        {"_id": ObjectId(alert_id)},
        {"$set": {"acknowledged": True}},
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Alert not found")
    return {"message": "Acknowledged"}


# routers/discharge.py — Discharge summary endpoints
discharge_router = APIRouter()


@discharge_router.get("/{patient_id}")
async def get_discharge_summary(patient_id: str):
    db = get_db()
    summary = await db.discharge_summaries.find_one(
        {"patient_id": patient_id}, {"_id": 0}
    )
    if not summary:
        raise HTTPException(status_code=404, detail="Discharge summary not found")
    return summary


@discharge_router.get("/")
async def list_discharge_summaries(limit: int = 20):
    db = get_db()
    summaries = await db.discharge_summaries.find(
        {}, {"_id": 0, "patient_id": 1, "patient_name": 1, "discharged_at": 1}
    ).to_list(length=limit)
    return {"summaries": summaries}
