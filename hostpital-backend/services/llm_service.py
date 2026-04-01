# services/llm_service.py — Google Gemini 1.5 Flash integration
import json
import re
import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini once at import time
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    _model = genai.GenerativeModel("gemini-1.5-flash")
else:
    _model = None
    print("WARNING: GEMINI_API_KEY not set — LLM calls will return mock data")


def _extract_json(text: str) -> dict:
    """Strip markdown fences and parse JSON from model response."""
    clean = re.sub(r"```(?:json)?|```", "", text).strip()
    return json.loads(clean)


async def analyse_patient(patient: dict, vitals: list) -> dict:
    """
    Send patient symptoms + vitals to Gemini and get structured clinical insights.
    Returns a dict with: summary, possible_condition, suggested_next_steps
    """
    if _model is None:
        return _mock_insights(patient)

    latest_vitals = vitals[-1] if vitals else "No vitals recorded yet"

    prompt = f"""You are a clinical decision support assistant helping a doctor in an emergency department.

Patient information:
- Name: {patient.get('name', 'Unknown')}
- Age: {patient.get('age', 'Unknown')}
- Reported symptoms: {', '.join(patient.get('symptoms', []))}
- Symptom description: {patient.get('symptom_text', 'None provided')}
- Priority score: {patient.get('priority_score', 0)} / 100
- Priority level: {patient.get('priority_level', 'unknown')}
- Latest vitals: {latest_vitals}

Based on the above, provide a clinical decision support summary.
Respond ONLY with a valid JSON object — no markdown, no explanation outside JSON:
{{
  "summary": "2–3 sentence clinical summary of the patient's presentation",
  "possible_condition": "Most likely diagnosis or differential diagnoses (concise)",
  "suggested_next_steps": "Recommended immediate actions for the attending doctor"
}}"""

    try:
        response = _model.generate_content(prompt)
        return _extract_json(response.text)
    except Exception as e:
        print(f"LLM error: {e}")
        return _mock_insights(patient)


async def assess_post_surgery_vitals(patient: dict, vitals: dict, rule_level: str) -> dict:
    """
    Called when rule-based check flags borderline vitals.
    Returns: { "alert_type": "warning"|"critical"|"none", "reasoning": "..." }
    """
    if _model is None:
        return {"alert_type": rule_level, "reasoning": "Mock LLM assessment"}

    prompt = f"""You are a post-surgery monitoring assistant.

Patient: {patient.get('name')}, Age {patient.get('age')}
Vitals reading: {json.dumps(vitals)}
Rule-based classification: {rule_level}

Assess whether this patient needs immediate intervention.
Respond ONLY with valid JSON:
{{
  "alert_type": "none" | "warning" | "critical",
  "reasoning": "One sentence explanation of your assessment"
}}"""

    try:
        response = _model.generate_content(prompt)
        return _extract_json(response.text)
    except Exception as e:
        print(f"LLM monitoring error: {e}")
        return {"alert_type": rule_level, "reasoning": "Fallback to rule-based assessment"}


def _mock_insights(patient: dict) -> dict:
    """Returned when no API key is configured — useful for local dev."""
    return {
        "summary": f"Patient presents with {', '.join(patient.get('symptoms', ['unspecified symptoms']))}. Priority level is {patient.get('priority_level', 'unknown')}. Further evaluation recommended.",
        "possible_condition": "Requires clinical evaluation — mock LLM response (no API key set)",
        "suggested_next_steps": "1. Complete physical examination. 2. Order relevant labs. 3. Monitor vitals every 30 minutes.",
    }
