from fastapi import APIRouter, HTTPException

from app.db.session import SessionDep
from app.db.models import Appointment
from app.schemas.appointments import AppointmentCreate

router = APIRouter(
    prefix="/appointments",
    tags=["appointments"]
)


@router.post("", response_model=Appointment)
def create_appointment(session: SessionDep, appointment: AppointmentCreate):
    
    session.add(Appointment.model_validate(appointment))
    
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=422, detail=e)

    session.refresh(appointment)
    return appointment


@router.get("/{appointment_id}", response_model=Appointment)
def get_appointment(appointment_id: int, session: SessionDep):
    return session.get(Appointment, appointment_id)
