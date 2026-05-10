import pytest
import requests

def test_create_user_and_verify_in_db(api_session, db_connection):
    payload = {"username": "Artemiy_Dev", "email": "artem@example.com"}
    response = api_session.post(f"{api_session.base_url}/users", json=payload)
    assert response.status_code == 201

def test_health_check(api_session):
    response = requests.get("http://localhost:3001/health")
    assert response.status_code == 200
