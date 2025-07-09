from fastapi.testclient import TestClient
from datatest import doctor

def test_1_create_doctor(client: TestClient):
    response = client.post("/doctors", json=doctor)
    print(response.text)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    data.pop("id")
    assert data == doctor


# def test_2_get_doctor(client: TestClient):
#     response = client.get("/doctors/1")
#     assert response.status_code == 200
#     data = response.json().pop("id")
#     assert data == doctor


# def test_3_error_get_doctor(client: TestClient):
#     response = client.get("/doctors/0")
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Doctor with id 0 was not found in database."}
