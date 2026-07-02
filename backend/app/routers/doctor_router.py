from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.doctor import DoctorCreate
from app.services.doctor_service import create_doctor, get_all_doctors
from app.database.dependency import get_db

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


@router.post("/")
def add_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db)
):
    return create_doctor(db, doctor)


@router.get("/")
def fetch_doctors(
    db: Session = Depends(get_db)
):
    return get_all_doctors(db)