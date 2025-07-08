from fastapi import APIRouter, HTTPException

from app.db.session import SessionDep
from app.db.models import Doctor

router = APIRouter(
    prefix="/doctors",
    tags=["doctors"]
)


@router.post("", response_model=Doctor)
def create_doctor(session: SessionDep, doctor: Doctor):
    session.add(doctor)
    
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=422, detail=e)
    
    session.refresh(doctor)
    return doctor


@router.get("/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int, session: SessionDep):
    return session.get(Doctor, doctor_id)
