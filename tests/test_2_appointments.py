from copy import copy

from datatest import (appointment_description, appointment_error_description,
                      appointment_for_response, appointment_time)
from fastapi.testclient import TestClient


def test_1_create_appointment(client: TestClient, prepared_doctor):
    response = client.post("/appointments", json=appointment_for_response)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    data.pop("id")
    assert data == appointment_for_response


def test_2_create_error_bad_description_appointment(
    client: TestClient, prepared_doctor
):
    bad_appointment = copy(appointment_for_response)
    bad_appointment.update({"description": appointment_error_description})
    response = client.post("/appointments", json=bad_appointment)
    assert response.status_code == 422
    assert (
        response.json().get("detail")[0].get("msg")
        == "String should have at most 3000 characters"
    )


def test_3_create_error_doctor_not_found_appointment(client: TestClient):
    response = client.post("/appointments", json=appointment_for_response)
    assert response.status_code == 404
    assert response.json() == {"detail": "Doctor with id 1 was not found in database."}


def test_4_create_error_same_doctor_and_time_appointment(
    client: TestClient, prepared_doctor
):
    client.post("/appointments", json=appointment_for_response)
    response = client.post("/appointments", json=appointment_for_response)
    assert response.status_code == 422
    assert response.json() == {
        "detail": "Doctor can't accept several appointments at the same time."
    }


def test_5_get_appointment(client: TestClient, prepared_appointment):
    response = client.get("/appointments/1")
    assert response.status_code == 200
    data = response.json()
    data.pop("id")
    assert data == {
        "doctor_id": 1,
        "description": appointment_description,
        "start_time": appointment_time.isoformat(),
    }


def test_6_get_error_non_existent_appointment(client: TestClient):
    response = client.get("/appointments/1")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Appointment with id 1 was not found in database."
    }
