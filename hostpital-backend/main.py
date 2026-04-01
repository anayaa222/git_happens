# main.py — FastAPI application entry point
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from database import connect_db, close_db
from routers import patient, nurse, doctor, queue, alerts, discharge
from services.monitoring import start_monitoring, stop_monitoring


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_db()
    await start_monitoring()
    yield
    # Shutdown
    await stop_monitoring()
    await close_db()


app = FastAPI(
    title="Hospital Patient Management System",
    description="API for patient management, priority triage, and LLM-assisted clinical decisions",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(patient.router, prefix="/api/patients", tags=["Patient"])
app.include_router(nurse.router,   prefix="/api/nurse",    tags=["Nurse"])
app.include_router(doctor.router,  prefix="/api/doctor",   tags=["Doctor"])
app.include_router(queue.router,   prefix="/api/queue",    tags=["Queue"])
app.include_router(alerts.router,  prefix="/api/alerts",   tags=["Alerts"])
app.include_router(discharge.router, prefix="/api/discharge", tags=["Discharge"])


@app.get("/", tags=["Health"])
async def health_check():
    return {"status": "ok", "message": "Hospital Management API is running"}
