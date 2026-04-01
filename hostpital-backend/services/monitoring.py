# services/monitoring.py — APScheduler post-surgery monitoring loop
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timezone

from config import MONITORING_INTERVAL_MINUTES
from database import get_db
from utils.vitals_rules import check_vitals
from services.llm_service import assess_post_surgery_vitals

_scheduler = AsyncIOScheduler()


async def run_post_surgery_checks():
    """
    Runs every MONITORING_INTERVAL_MINUTES minutes.
    Finds all patients in 'monitoring' status, fetches their latest vitals,
    applies rule-based check, then optionally escalates to LLM.
    """
    db = get_db()
    if db is None:
        return

    monitoring_patients = await db.patients.find(
        {"status": "monitoring"}
    ).to_list(length=None)

    for patient in monitoring_patients:
        pid = patient["patient_id"]

        # Fetch latest vitals
        latest = await db.vitals.find_one(
            {"patient_id": pid, "is_post_surgery": True},
            sort=[("recorded_at", -1)],
        )

        if not latest:
            continue

        # Step 1: Rule-based check (fast, no API call)
        rule_level, rule_message = check_vitals(latest)

        if rule_level is None:
            # All normal — no alert needed
            continue

        final_level = rule_level
        final_message = rule_message

        # Step 2: If warning (borderline), ask LLM for context-aware assessment
        if rule_level == "warning":
            llm_result = await assess_post_surgery_vitals(patient, latest, rule_level)
            final_level   = llm_result.get("alert_type", rule_level)
            final_message = f"{rule_message} — LLM: {llm_result.get('reasoning', '')}"

        # Step 3: If critical, fire immediately without waiting for LLM
        if final_level in ("warning", "critical"):
            target_role = "doctor" if final_level == "critical" else "nurse"
            alert = {
                "patient_id":  pid,
                "type":        final_level,
                "message":     f"[Post-surgery] {final_message}",
                "target_role": target_role,
                "acknowledged": False,
                "created_at":  datetime.now(timezone.utc),
            }
            await db.alerts.insert_one(alert)
            print(f"Alert created for {pid}: [{final_level}] {final_message}")


async def start_monitoring():
    _scheduler.add_job(
        run_post_surgery_checks,
        trigger="interval",
        minutes=MONITORING_INTERVAL_MINUTES,
        id="post_surgery_monitor",
        replace_existing=True,
    )
    _scheduler.start()
    print(f"Post-surgery monitoring started (every {MONITORING_INTERVAL_MINUTES} min)")


async def stop_monitoring():
    if _scheduler.running:
        _scheduler.shutdown()
        print("Monitoring scheduler stopped")
