from unittest.mock import patch

import pytest


@pytest.fixture()
def valid_payload():
    return {"input": "kitties for everyone"}


@patch("src.services.v1.images_service.ImageFromAIService.get_image")
def test_get_image_from_openai(
    mock_service, client, json_header, valid_payload
):
    expected_from_service = "This is a mocked templated"
    mock_service.return_value = expected_from_service
    response = client.post(
        "/v1/generate-img-from-ai/", headers=json_header, json=valid_payload
    )

    assert response.status_code == 200
    assert response.text == "This is a mocked templated"
    assert response.is_success
    assert not response.is_error
