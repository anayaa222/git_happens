# services/scoring.py — Priority score calculation
from models.patient_model import SYMPTOM_WEIGHTS, PriorityLevel


def calculate_priority_score(symptoms: list[str]) -> int:
    """Sum weights for each recognised symptom. Unknown keys score 0."""
    return sum(SYMPTOM_WEIGHTS.get(s, 0) for s in symptoms)


def classify_priority(score: int) -> PriorityLevel:
    """
    0–30  → Low
    31–60 → Medium
    61+   → High (Emergency)
    """
    if score >= 61:
        return PriorityLevel.high
    elif score >= 31:
        return PriorityLevel.medium
    else:
        return PriorityLevel.low
