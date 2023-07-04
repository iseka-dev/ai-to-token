import pytest
from fastapi.testclient import TestClient

from src.config import settings
from src.main import app
from src.schemas.v1.schemas import PromptRequest

client = TestClient(app)


@pytest.fixture()
def client():
    client = TestClient(app)
    yield client


@pytest.fixture()
def json_header():
    return {"Content-Type": "application/json"}


@pytest.fixture()
def openai_json_header():
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
    }


@pytest.fixture()
def prompt_payload_dict():
    return {"prompt": "kitties for everyone"}


@pytest.fixture()
def prompt_payload_schema():
    return PromptRequest(
        prompt="kitties for everyone"
    )
