# models/patient_model.py — Pydantic request/response schemas
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class PriorityLevel(str, Enum):
    low    = "low"
    medium = "medium"
    high   = "high"


class PatientStatus(str, Enum):
    waiting    = "waiting"
    admitted   = "admitted"
    surgery    = "surgery"
    monitoring = "monitoring"
    discharged = "discharged"


# --- Symptom weights used by scoring service ---
SYMPTOM_WEIGHTS = {
    "chest_pain":           30,
    "shortness_of_breath":  25,
    "severe_bleeding":      28,
    "loss_of_consciousness":35,
    "stroke_symptoms":      40,
    "high_fever":           15,
    "severe_abdominal_pain":20,
    "trauma":               22,
    "nausea_vomiting":       8,
    "dizziness":             7,
    "headache":              5,
    "fatigue":               3,
    "mild_fever":            6,
    "cough":                 4,
    "sore_throat":           3,
}


class RegisterPatientRequest(BaseModel):
    name:          str
    age:           int             = Field(..., ge=0, le=130)
    symptoms:      List[str]       = Field(..., description="List of symptom keys from SYMPTOM_WEIGHTS")
    symptom_text:  str             = Field("", description="Free-text symptom description")
    contact_phone: Optional[str]  = None


class LLMInsights(BaseModel):
    summary:               str
    possible_condition:    str
    suggested_next_steps:  str
    generated_at:          datetime = Field(default_factory=datetime.utcnow)


class DoctorDecision(BaseModel):
    approved_llm:  bool
    notes:         str
    prescription:  Optional[str] = None
    decided_at:    datetime = Field(default_factory=datetime.utcnow)


class AssignRequest(BaseModel):
    bed_id:             Optional[str] = None
    nurse_id:           Optional[str] = None
    doctor_id:          Optional[str] = None
    surgery_scheduled:  Optional[datetime] = None


class DecisionRequest(BaseModel):
    approved_llm: bool
    notes:        str
    prescription: Optional[str] = None
