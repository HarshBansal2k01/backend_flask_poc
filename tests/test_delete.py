import json
import pytest
from Delivery_backend.app import app, User


# Define a test to delete a user
def test_delete_user():
    # Create a test client for the Flask app
    client = app.test_client()

    # Define a sample email for a user to delete
    email_to_delete = "hbbro14@gmail.com"

    # Send a DELETE request to the /delete/<email> endpoint with the sample email
    response = client.delete(f"/delete/{email_to_delete}")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check the response JSON to ensure it indicates a successful user deletion
    response_data = json.loads(response.data)
    assert response_data["success"] is True
    assert response_data["message"] == "User Deleted successfully"


# Add a test to delete a user that does not exist
def test_delete_user_not_found():
    client = app.test_client()

    email_to_delete = "nonexistent@example.com"

    response = client.delete(f"/delete/{email_to_delete}")

    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert response_data["success"] is False
    assert response_data["message"] == "User not found in the database"
