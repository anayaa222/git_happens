# models/vitals_model.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class VitalsRequest(BaseModel):
    bp_systolic:        int   = Field(..., ge=40,  le=300)
    bp_diastolic:       int   = Field(..., ge=20,  le=200)
    heart_rate:         int   = Field(..., ge=20,  le=300)
    oxygen_saturation:  float = Field(..., ge=50.0, le=100.0)
    temperature:        float = Field(..., ge=30.0, le=45.0)  # Celsius
    is_post_surgery:    bool  = False
    recorded_by:        Optional[str] = None


class VitalsResponse(BaseModel):
    patient_id:         str
    bp_systolic:        int
    bp_diastolic:       int
    heart_rate:         int
    oxygen_saturation:  float
    temperature:        float
    is_post_surgery:    bool
    alert_triggered:    Optional[str]   # None | "warning" | "critical"
    recorded_at:        datetime


# models/alert_model.py
class AlertType(str):
    warning  = "warning"
    critical = "critical"


class AlertCreate(BaseModel):
    patient_id:  str
    type:        str          # "warning" | "critical"
    message:     str
    target_role: str          # "nurse" | "doctor"


class AlertResponse(BaseModel):
    id:           str
    patient_id:   str
    type:         str
    message:      str
    target_role:  str
    acknowledged: bool
    created_at:   datetime
