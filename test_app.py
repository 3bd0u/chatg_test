# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Bienvenue sur mon API Flask !"

def test_add(client):
    response = client.get("/add/3/5")
    assert response.status_code == 200
    assert response.json["result"] == 8
