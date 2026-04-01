# utils/vitals_rules.py — Rule-based alert threshold checker
from config import VITALS_THRESHOLDS


def check_vitals(vitals: dict) -> tuple[str | None, str]:
    """
    Evaluate a vitals reading against configured thresholds.
    Returns: (alert_level, message)
        alert_level: None | "warning" | "critical"
    Checks in order — returns the HIGHEST severity found.
    """
    issues = []

    t = VITALS_THRESHOLDS

    o2 = vitals.get("oxygen_saturation", 100)
    if o2 <= t["oxygen_saturation"]["critical"]:
        issues.append(("critical", f"O₂ saturation critically low ({o2}%)"))
    elif o2 <= t["oxygen_saturation"]["warning"]:
        issues.append(("warning", f"O₂ saturation low ({o2}%)"))

    hr = vitals.get("heart_rate", 70)
    if hr >= t["heart_rate_high"]["critical"]:
        issues.append(("critical", f"Heart rate critically high ({hr} bpm)"))
    elif hr >= t["heart_rate_high"]["warning"]:
        issues.append(("warning", f"Heart rate elevated ({hr} bpm)"))
    elif hr <= t["heart_rate_low"]["critical"]:
        issues.append(("critical", f"Heart rate critically low ({hr} bpm)"))
    elif hr <= t["heart_rate_low"]["warning"]:
        issues.append(("warning", f"Heart rate low ({hr} bpm)"))

    sys_bp = vitals.get("bp_systolic", 120)
    if sys_bp >= t["bp_systolic_high"]["critical"]:
        issues.append(("critical", f"BP critically high ({sys_bp} mmHg systolic)"))
    elif sys_bp >= t["bp_systolic_high"]["warning"]:
        issues.append(("warning", f"BP elevated ({sys_bp} mmHg systolic)"))
    elif sys_bp <= t["bp_systolic_low"]["critical"]:
        issues.append(("critical", f"BP critically low ({sys_bp} mmHg systolic)"))
    elif sys_bp <= t["bp_systolic_low"]["warning"]:
        issues.append(("warning", f"BP low ({sys_bp} mmHg systolic)"))

    temp = vitals.get("temperature", 37.0)
    if temp >= t["temperature_high"]["critical"]:
        issues.append(("critical", f"Temperature critically high ({temp}°C)"))
    elif temp >= t["temperature_high"]["warning"]:
        issues.append(("warning", f"Temperature elevated ({temp}°C)"))
    elif temp <= t["temperature_low"]["critical"]:
        issues.append(("critical", f"Temperature critically low ({temp}°C)"))
    elif temp <= t["temperature_low"]["warning"]:
        issues.append(("warning", f"Temperature low ({temp}°C)"))

    if not issues:
        return None, "All vitals normal"

    # Return highest severity
    if any(level == "critical" for level, _ in issues):
        msgs = [msg for level, msg in issues if level == "critical"]
        return "critical", "; ".join(msgs)
    else:
        msgs = [msg for _, msg in issues]
        return "warning", "; ".join(msgs)
