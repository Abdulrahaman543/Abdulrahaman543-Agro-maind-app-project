import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ai_chat_text_response():
    response = client.post("/api/v1/ai_chat/text", json={"message": "What is the best crop for my region?"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_ai_chat_voice_response():
    response = client.post("/api/v1/ai_chat/voice", json={"audio": "base64_encoded_audio"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_ai_chat_invalid_input():
    response = client.post("/api/v1/ai_chat/text", json={"message": ""})
    assert response.status_code == 400
    assert "detail" in response.json()