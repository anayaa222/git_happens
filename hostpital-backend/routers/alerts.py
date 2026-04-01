# routers/alerts.py
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from database import get_db

router = APIRouter()


@router.get("/")
async def get_all_alerts(role: str = None, acknowledged: bool = False):
    """Get alerts, optionally filtered by role (nurse / doctor)."""
    db = get_db()
    query: dict = {"acknowledged": acknowledged}
    if role:
        query["target_role"] = role
    alerts = await db.alerts.find(
        query, {"_id": 0}, sort=[("created_at", -1)]
    ).to_list(length=100)
    return {"alerts": alerts, "count": len(alerts)}


@router.put("/{alert_id}/acknowledge")
async def acknowledge_alert(alert_id: str):
    """Mark an alert as acknowledged by ID."""
    db = get_db()
    result = await db.alerts.update_one(
        {"_id": ObjectId(alert_id)},
        {"$set": {"acknowledged": True}},
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Alert not found")
    return {"message": "Alert acknowledged"}
