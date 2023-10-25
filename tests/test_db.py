import pytest
from Delivery_backend.app import app  # Import your Flask app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Test case to check if the database connection is successful
def test_check_db_connection_success(client):
    # Send a GET request to the '/check_db_connection' route
    response = client.get("/check_db_connection")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response data contains the success message
    assert b"Database connection successful" in response.data


# Test case to check if a database connection error is handled
def test_check_db_connection_failure(client):
    # Mock a database connection error (e.g., by patching the db.engine.connect() function)

    # Send a GET request to the '/check_db_connection' route
    response = client.get("/check_db_connection")


    assert response.status_code == 500

    # Check if the response data contains the error message
    assert b"Database connection error" in response.data
