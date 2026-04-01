# config.py — Environment configuration
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB
MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME:   str = os.getenv("DB_NAME", "hospital_db")

# Google Gemini
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

# Security
SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-in-production")

# Monitoring
MONITORING_INTERVAL_MINUTES: int = int(os.getenv("MONITORING_INTERVAL_MINUTES", "10"))

# Alert thresholds (rule-based)
VITALS_THRESHOLDS = {
    "oxygen_saturation": {"warning": 92, "critical": 88},      # below these → alert
    "heart_rate_high":   {"warning": 120, "critical": 140},     # above these → alert
    "heart_rate_low":    {"warning": 50,  "critical": 40},      # below these → alert
    "bp_systolic_high":  {"warning": 160, "critical": 180},
    "bp_systolic_low":   {"warning": 85,  "critical": 70},
    "temperature_high":  {"warning": 38.5,"critical": 39.5},    # Celsius
    "temperature_low":   {"warning": 35.5,"critical": 34.5},
}
