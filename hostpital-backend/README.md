# Hospital Patient Management System — Backend

FastAPI + MongoDB + Google Gemini LLM backend for a hospital patient management and clinical decision support system.

---

## Quick Start

### 1. Clone & set up virtual environment
```bash
git clone <your-repo-url>
cd hospital-backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment
```bash
cp .env.example .env
# Edit .env with your MongoDB URI and Gemini API key
```

### 3. Get your free Gemini API key
- Visit: https://aistudio.google.com
- Sign in with Google → click "Get API key" → Create API key
- Paste into `.env` as `GEMINI_API_KEY=...`

### 4. Set up MongoDB Atlas (free)
- Visit: https://cloud.mongodb.com
- Create a free M0 cluster
- Database Access → Add user with read/write permissions
- Network Access → Add your IP (or 0.0.0.0/0 for dev)
- Connect → Drivers → Copy connection string into `.env` as `MONGO_URI=...`

### 5. Run the server
```bash
uvicorn main:app --reload --port 8000
```

### 6. Open API docs
- Swagger UI: http://localhost:8000/docs
- ReDoc:       http://localhost:8000/redoc

---

## Project Structure

```
hospital-backend/
├── main.py                  # FastAPI entry point, CORS, lifespan
├── config.py                # Env vars, alert thresholds
├── database.py              # Motor async MongoDB client + GridFS
├── requirements.txt
├── render.yaml              # Render.com deployment config
├── .env.example
│
├── routers/
│   ├── patient.py           # POST /register, GET /{id}, GET /{id}/status
│   ├── nurse.py             # vitals, file upload, nurse alerts
│   ├── doctor.py            # queue, LLM insights, decisions, discharge
│   ├── queue.py             # bed status, reprioritise
│   ├── alerts.py            # get & acknowledge alerts
│   └── discharge.py         # discharge summaries
│
├── models/
│   ├── patient_model.py     # RegisterPatientRequest, SYMPTOM_WEIGHTS, enums
│   └── vitals_model.py      # VitalsRequest, AlertCreate, AlertResponse
│
├── services/
│   ├── llm_service.py       # Gemini 1.5 Flash integration
│   ├── scoring.py           # Priority score formula
│   └── monitoring.py        # APScheduler post-surgery monitoring loop
│
└── utils/
    ├── id_generator.py      # PAT-YYYYMMDD-XXXXX generator
    └── vitals_rules.py      # Rule-based alert threshold checker
```

---

## API Reference

### Patient Panel
| Method | Route | Description |
|--------|-------|-------------|
| POST | `/api/patients/register` | Register patient, score symptoms, return patient_id |
| GET  | `/api/patients/{id}` | Full patient record |
| GET  | `/api/patients/{id}/status` | Queue position + assigned resources |
| GET  | `/api/patients/{id}/discharge-report` | Discharge summary |

### Nurse Panel
| Method | Route | Description |
|--------|-------|-------------|
| GET  | `/api/nurse/assigned-patients?nurse_id=X` | List assigned patients |
| POST | `/api/nurse/vitals/{patient_id}` | Submit vitals reading |
| GET  | `/api/nurse/vitals/{patient_id}` | Vitals history |
| POST | `/api/nurse/upload-report/{patient_id}` | Upload PDF/image |
| GET  | `/api/nurse/alerts` | Active nurse alerts |
| PUT  | `/api/nurse/alerts/{id}/acknowledge` | Acknowledge alert |

### Doctor Panel
| Method | Route | Description |
|--------|-------|-------------|
| GET  | `/api/doctor/queue` | Priority-sorted patient queue |
| GET  | `/api/doctor/patient/{id}/llm-insights` | Gemini analysis (cached or fresh) |
| POST | `/api/doctor/patient/{id}/decision` | Approve/reject LLM, add notes |
| POST | `/api/doctor/patient/{id}/assign` | Assign bed, nurse, surgery |
| POST | `/api/doctor/patient/{id}/discharge` | Discharge patient |
| GET  | `/api/doctor/alerts` | Critical alerts for doctor |

### Queue & Alerts
| Method | Route | Description |
|--------|-------|-------------|
| GET  | `/api/queue/beds` | Bed availability |
| POST | `/api/queue/trigger-llm/{id}` | Force-refresh LLM insights |
| GET  | `/api/alerts/?role=nurse` | All alerts filtered by role |
| PUT  | `/api/alerts/{id}/acknowledge` | Acknowledge any alert |

---

## Priority Scoring

Symptoms have pre-assigned weights. Score = sum of matching symptom weights.

| Score Range | Level |
|-------------|-------|
| 0 – 30 | Low |
| 31 – 60 | Medium |
| 61+ | High / Emergency |

**Top-weight symptoms:** loss_of_consciousness (35), stroke_symptoms (40), chest_pain (30), severe_bleeding (28), shortness_of_breath (25).

---

## Post-Surgery Monitoring

APScheduler fires every 10 minutes (configurable via `MONITORING_INTERVAL_MINUTES`).

Flow:
1. Find all patients with `status = "monitoring"`
2. Fetch latest post-surgery vitals
3. Run rule-based check (fast, no API call)
4. If **warning** → call Gemini for context-aware assessment
5. If **critical** → fire alert immediately, skip LLM
6. Insert alert into `alerts` collection targeting nurse (warning) or doctor (critical)

---

## Alert Thresholds

Configurable in `config.py → VITALS_THRESHOLDS`:

| Vital | Warning | Critical |
|-------|---------|----------|
| O₂ Saturation | < 92% | < 88% |
| Heart Rate (high) | > 120 bpm | > 140 bpm |
| Heart Rate (low) | < 50 bpm | < 40 bpm |
| BP Systolic (high) | > 160 mmHg | > 180 mmHg |
| BP Systolic (low) | < 85 mmHg | < 70 mmHg |
| Temperature (high) | > 38.5°C | > 39.5°C |
| Temperature (low) | < 35.5°C | < 34.5°C |

---

## Deployment (Render.com)

1. Push this folder to GitHub
2. Go to render.com → New Web Service → Connect repo
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables: `MONGO_URI`, `GEMINI_API_KEY`, `SECRET_KEY`
6. Deploy — your API will be live at `https://your-app.onrender.com`

Alternatively, use the included `render.yaml` for one-click deploy.

---

## Testing Without Gemini Key

If `GEMINI_API_KEY` is not set, the LLM service returns mock insights automatically. All other features (registration, vitals, alerts, queue) work fully without any API key.

---

## MongoDB Collections

- `patients` — core patient records
- `vitals` — time-series vitals readings
- `alerts` — warning and critical alerts
- `discharge_summaries` — complete discharge records
- GridFS buckets — uploaded PDF/image reports
