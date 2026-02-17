from fastapi import HTTPException
from app.api.v1.auth import authenticate_user, create_user
from app.models.user import User
from app.schemas.index import UserCreate
import pytest

@pytest.fixture
def test_user():
    return UserCreate(username="testuser", password="testpassword", age=25, country="Testland", id_number="123456789")

def test_create_user(client, test_user):
    response = client.post("/api/v1/auth/register", json=test_user.dict())
    assert response.status_code == 201
    assert response.json()["username"] == test_user.username

def test_authenticate_user(client, test_user):
    client.post("/api/v1/auth/register", json=test_user.dict())
    response = client.post("/api/v1/auth/login", json={"username": test_user.username, "password": test_user.password})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_authenticate_user_invalid(client):
    response = client.post("/api/v1/auth/login", json={"username": "invaliduser", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"