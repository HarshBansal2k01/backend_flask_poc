import json
import pytest
from Delivery_backend.app import app  # Import your Flask app and database setup


# Define a test to check if an email exists in the database
def test_check_email():
    # Create a test client for the Flask app
    client = app.test_client()

    # Define a sample email to check
    email_to_check = "hbbro14@gmail.com"

    # Send a POST request to the /check-email endpoint with the sample data
    response = client.post("/check-email", json={"email_address": email_to_check})

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check the response JSON to ensure it indicates whether the email is found
    response_data = json.loads(response.data)
    assert response_data["success"] is True
    assert response_data["message"] == "Email found in the database"


# Add another test to check when the email is not found
def test_check_email_not_found():
    client = app.test_client()

    email_to_check = "nonexistent@example.com"

    response = client.post("/check-email", json={"email_address": email_to_check})

    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert response_data["success"] is False
    assert response_data["message"] == "Email not found in the database"


def test_check_email_invalid_input():
    client = app.test_client()

    response = client.post("/check-email", json={})

    assert response.status_code == 400

    response_data = json.loads(response.data)
    assert response_data["success"] is False
    assert response_data["message"] == "Invalid input data"


def test_check_email_internal_server_error():
    client = app.test_client()

    response = client.post("/check-email", data="Invalid JSON Data")

    assert response.status_code == 500

    response_data = json.loads(response.data)
    assert (
        response_data["error"] == "Internal Server Error: Failed to add delivery data"
    )
