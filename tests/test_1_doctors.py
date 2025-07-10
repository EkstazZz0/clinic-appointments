import random

from datatest import (
    doctor_error_create,
    doctor_error_create_response,
    doctor_for_response,
)
from fastapi.testclient import TestClient


def test_1_create_doctor(client: TestClient):
    response = client.post("/doctors", json=doctor_for_response)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    data.pop("id")
    assert data == doctor_for_response


def test_2_create_error_doctor(client: TestClient):
    response = client.post("/doctors", json=doctor_error_create)
    assert response.status_code == 422
    assert response.json() == doctor_error_create_response


def test_3_get_doctor(client: TestClient, prepared_doctor):
    response = client.get("/doctors/1")
    assert response.status_code == 200
    data = response.json()
    data.pop("id")
    assert data == doctor_for_response


def test_4_get_error_doctor(client: TestClient):
    for _ in range(10):
        doctor_id = random.randint(-5, 5)
        response = client.get(f"/doctors/{doctor_id}")
        assert response.status_code == 404
        assert response.json() == {
            "detail": f"Doctor with id {doctor_id} was not found in database."
        }
