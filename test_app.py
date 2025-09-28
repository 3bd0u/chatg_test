# test_app.py
import requests

def test_example():
    """Un test basique qui vérifie une addition"""
    assert 1 + 1 == 2

def test_github_api():
    """Un test qui vérifie que l'API GitHub répond"""
    response = requests.get("https://api.github.com")
    assert response.status_code == 200
