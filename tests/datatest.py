from datetime import datetime, timedelta

doctor_for_response = {
    "name": "Иванов Иван Иванович",
    "birth_date": "1990-05-11"
}

doctor_error_create = {
    "name": "s" * 151,
    "birth_date": "1990-05-11"
}

doctor_error_create_response = {
    "detail": [{
        "type":"string_too_long",
        "loc":["body","name"],
        "msg":"String should have at most 150 characters",
        "input":"s" * 151,
        "ctx":{"max_length":150}}]
}

doctor_for_db = {
    "name": "Иванов Иван Иванович",
    "birth_date": datetime.strptime("1990-05-11", "%Y-%m-%d").date()
}

appointment_for_response = {
    "doctor_id": 1,
    "description": "real important appointment",
    "start_time": "2025-08-25T15:00:00"
}

appointment_time = datetime.now() + timedelta(days=60)
appointment_description = "some desc"
appointment_error_description = "s" * 3001