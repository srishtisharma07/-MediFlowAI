from fastapi import FastAPI

from app.database.database import engine
from app.database.base import Base

from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.appointment import Appointment
from app.routers.doctor_router import router as doctor_router
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MediFlow AI",
    version="1.0.0"
)

app.include_router(doctor_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to MediFlow AI Backend"
    }