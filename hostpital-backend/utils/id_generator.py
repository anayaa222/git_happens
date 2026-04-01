# utils/id_generator.py — Unique Patient ID generation
import random
import string
from datetime import datetime


def generate_patient_id() -> str:
    """
    Format: PAT-YYYYMMDD-XXXXX
    Example: PAT-20241215-A7K3M
    Collision probability is negligible for hospital-scale usage.
    """
    date_part   = datetime.utcnow().strftime("%Y%m%d")
    random_part = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"PAT-{date_part}-{random_part}"
