import pytest
from Delivery_backend.app import app, db, get_users, User
from flask import jsonify


def test_User_200():
    client = app.test_client()

    # Make a request to your route
    response = client.get("/users")

    assert response.status_code == 200
    assert response.content_type == "application/json"

    data = response.get_json()

    for item in data:
        assert "email_address" in item
        assert "id" in item
        assert "phone_no" in item
        assert "pincode" in item


def test_Pickup_200():
    client = app.test_client()

    response = client.get("/pickup")

    assert response.status_code == 200
    assert response.content_type == "application/json"

    data = response.get_json()

    for item in data:
        assert "id" in item
        assert "Name" in item
        assert "phone_no" in item
        assert "email" in item
        assert "pincode" in item
        assert "pickuplocation" in item
        assert "preferred_time" in item


def test_Delivery_200():
    client = app.test_client()

    response = client.get("/delivery")

    assert response.status_code == 200
    assert response.content_type == "application/json"

    data = response.get_json()

    for item in data:
        assert "id" in item
        assert "name" in item
        assert "phone_no" in item
        assert "email" in item
        assert "address" in item
        assert "pincode" in item
