from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("patients.id"))

    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    appointment_date = Column(String, nullable=False)

    appointment_time = Column(String, nullable=False)

    reason = Column(String)

    status = Column(String, default="Booked")