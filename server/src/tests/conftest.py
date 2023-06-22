import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


@pytest.fixture()
def client():
    client = TestClient(app)
    yield client
