from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.db.session import SessionDep
from app.db.models import Appointment, Doctor
from app.schemas.appointments import AppointmentCreate

router = APIRouter(
    prefix="/appointments",
    tags=["appointments"]
)


@router.post("", response_model=Appointment)
def create_appointment(session: SessionDep, appointment: AppointmentCreate):

    if not session.get(Doctor, appointment.doctor_id):
        raise HTTPException(status_code=404, detail=f"Doctor with id {appointment.doctor_id} was not found in database")

    db_appointment = Appointment.model_validate(appointment)

    session.add(db_appointment)

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=422, detail="Doctor can't accept several appointments at the same time")

    session.refresh(db_appointment)
    return db_appointment


@router.get("/{appointment_id}", response_model=Appointment)
def get_appointment(appointment_id: int, session: SessionDep):
    return session.get(Appointment, appointment_id)
