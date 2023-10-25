import json
import pytest
from Delivery_backend.app import app, db  # Import your Flask app and database setup


# -------------------------------Delivery--------------------

# Define a test to create a delivery
def test_delivery_200():
    # Create a test client for the Flask app
    client = app.test_client()

    # Define a sample delivery data as a dictionary
    delivery_data = {
        "name": "John Doe",
        "phone_no": "1234567890",
        "email": "johndoe@example.com",
        "address": "123 Main St",
        "pincode": "12345",
    }

    # Send a POST request to the /delivery endpoint with the sample data
    response = client.post("/delivery", json=delivery_data)

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check the response JSON to ensure the data was added successfully
    response_data = json.loads(response.data)
    assert response_data == {"message": "Delivery data added successfully"}


def test_delivery_500():
    client = app.test_client()

    delivery_data = {
        "name": "John Doe",
        "phone_no": "1234567890",
        "email": "johndoe@example.com",
        "address": "123 Main St",
        # "pincode": "12345",
    }

    response = client.post("/delivery", json=delivery_data)

    assert response.status_code == 500

    response_data = json.loads(response.data)
    assert response_data == {
        "error": "Internal Server Error: Failed to add delivery data"
    }


# -------------------------------pickup--------------------


def test_Pickup_200():
    client = app.test_client()

    delivery_data = {
        "name": "John Doe",
        "phone_no": "1234567890",
        "email": "johndoe@example.com",
        "address": "123 Main St",
        "pincode": "12345",
        "pickuplocation": "assam",
        "preferred_time": "2023-10-24 15:30:00",
    }

    response = client.post("/pickup", json=delivery_data)

    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert response_data == {"message": "Pickup data added successfully"}


def test_Pickup_500():
    client = app.test_client()

    delivery_data = {
        "name": "John Doe",
        "phone_no": "1234567890",
        "email": "johndoe@example.com",
        "address": "123 Main St",
        "pincode": "12345",
        # "pickuplocation": "assam",
        # "preferred_time": "2023-10-24 15:30:00",
    }

    response = client.post("/pickup", json=delivery_data)

    assert response.status_code == 500

    response_data = json.loads(response.data)
    assert response_data == {
        "error": "Internal Server Error: Failed to add delivery data"
    }
