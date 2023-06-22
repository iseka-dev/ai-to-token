import os
import pytest

from fastapi.testclient import TestClient

from src.main import app

print(os.getcwd())

client = TestClient(app)


@pytest.fixture()
def client():
    client = TestClient(app)
    yield client


def test_get_health_check_route(client):
    response = client.get("/health-check")
    print(response)
    assert response.status_code == 200
    assert response.json() == {
        "check": {"server": "OK", "database": "OK"}
    }
