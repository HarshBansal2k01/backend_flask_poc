import json
import pytest
from Delivery_backend.app import app


def test_update_user():
    client = app.test_client()

    user_id_to_update = 14

    update_data = {
        "phone_no": "1234567890",
        "pincode": "54321",
        "email_address": "newemail@example.com",
    }

    response = client.put(f"/update-user/{user_id_to_update}", json=update_data)

    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert response_data["success"] is True
    assert response_data["message"] == "User updated successfully"


def test_update_user_not_found():
    client = app.test_client()

    non_existent_user_id = 999

    update_data = {
        "phone_no": "1234567890",
        "pincode": "54321",
        "email_address": "newemail@example.com",
    }

    response = client.put(f"/update-user/{non_existent_user_id}", json=update_data)

    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert response_data["success"] is False
    assert response_data["message"] == "User not found in the database"


def test_Invalid_input():
    client = app.test_client()

    non_existent_user_id = 14
    update_data = {
        "phone_no": "1234567890",
        "pincode": "54321",
    }

    response = client.put(f"/update-user/{non_existent_user_id}", json=update_data)

    assert response.status_code == 400

    response_data = json.loads(response.data)
    assert response_data["success"] is False
    assert response_data["message"] == "Invalid input data"


def test_internal_server_error():
    client = app.test_client()

    non_existent_user_id = 14

    update_data = {
        "phone_no": "1234567890",
        "pincode": "5432",
        # "email_address": "newemail@example.com",
    }

    response = client.put(f"/update-user/{non_existent_user_id}", json=update_data)

    assert response.status_code == 400

    response_data = json.loads(response.data)
    assert (
        response_data["message"] == "Internal Server Error: Failed to add delivery data"
    )
