import pytest
from fastapi.testclient import TestClient

from datatest import appointment_description, appointment_time, doctor_for_db

from app.db.models import Appointment, Doctor
from app.db.session import get_session
from app.main import app


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
        start_time=appointment_time,
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
