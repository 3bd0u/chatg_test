import pytest
from app import app  # Assure-toi que ton fichier principal s'appelle app.py

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test de la route principale"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Flask API is running!" in response.data

def test_api(client):
    """Test de la route JSON"""
    response = client.get("/api/test")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "API test successful 🚀"
