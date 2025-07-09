import pytest
from sqlmodel import create_engine, SQLModel, Session
from fastapi.testclient import TestClient
from fastapi import FastAPI
import os
from datetime import datetime

os.environ["APP_ENV"] = "test"

from app.main import app
from app.db.session import get_session
from app.db.models import Doctor, Appointment
from datatest import doctor_for_db, appointment_description, appointment_time

@pytest.fixture
def prepared_doctor():
    session_generator = get_session()
    session = next(session_generator)
    db_doctor = Doctor(**doctor_for_db)

    session.add(db_doctor)
    session.commit()
    session.refresh(db_doctor)

    yield db_doctor

    session.delete(db_doctor)
    session.commit()

    try:
        next(session_generator)
    except StopIteration:
        pass


@pytest.fixture
def prepared_appointment(prepared_doctor):
    session_generator = get_session()
    session = next(session_generator)

    db_appointment = Appointment(
        doctor_id=prepared_doctor.id,
        description=appointment_description,
        start_time=appointment_time
    )

    session.add(db_appointment)
    session.commit()
    session.refresh(db_appointment)

    yield db_appointment

    session.delete(db_appointment)
    session.commit()

    try:
        next(session_generator)
    except StopIteration:
        pass


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
