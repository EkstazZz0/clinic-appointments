from fastapi import APIRouter, HTTPException

from app.db.session import SessionDep
from app.db.models import Doctor
from app.schemas.doctors import DoctorCreate

router = APIRouter(
    prefix="/doctors",
    tags=["doctors"]
)


@router.post("", response_model=Doctor)
def create_doctor(session: SessionDep, doctor: DoctorCreate):
    db_doctor = Doctor.model_validate(doctor)
    session.add(db_doctor)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=422, detail=str(e))
    
    session.refresh(db_doctor)
    return db_doctor


@router.get("/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int, session: SessionDep):
    doctor = session.get(Doctor, doctor_id)
    if doctor:
        return doctor
    else:
        raise HTTPException(status_code=404, detail=f"Doctor with id {doctor_id} was not found in database.")
