from sqlalchemy.orm import Session
from app.models.doctor import Doctor


def create_doctor(db: Session, doctor):
    new_doctor = Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        experience=doctor.experience,
        fees=doctor.fees,
    )

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return new_doctor


def get_all_doctors(db: Session):
    return db.query(Doctor).all()