from unittest.mock import patch

from src.core.logger import log
from src.exceptions import OpenAIApiRateLimitExceeded

exception_message = "This is an exception"


@patch("src.services.v1.images_service.ImageFromAIService.generate_image")
def test_generate_image_from_openai_success(
    mock_service, client, json_header, prompt_payload_dict
):
    expected_from_service = "This is a mocked templated"
    mock_service.return_value = expected_from_service
    response = client.post(
        "/v1/generate-img-from-ai/",
        headers=json_header,
        json=prompt_payload_dict
    )

    assert response.status_code == 200
    assert response.text == expected_from_service
    assert response.is_success


@patch("src.services.v1.images_service.ImageFromAIService.generate_image")
def test_generate_image_from_openai_rate_limit(
    mock_service, client, json_header, prompt_payload_dict
):
    mock_service.side_effect = OpenAIApiRateLimitExceeded(exception_message)
    response = client.post(
        "/v1/generate-img-from-ai/",
        headers=json_header,
        json=prompt_payload_dict
    )

    assert response.status_code == 429
    assert response.json() == {
        "detail": {"Error": f"Error at image generation: {exception_message}"}
    }
    assert response.is_error


@patch("src.services.v1.images_service.ImageFromAIService.generate_image")
def test_generate_image_from_openai_missing_argument(
    mock_service, client, json_header
):
    mock_service.side_effect = OpenAIApiRateLimitExceeded(exception_message)
    response = client.post(
        "/v1/generate-img-from-ai/",
        headers=json_header,
        json={}
    )

    assert response.status_code == 422
    assert response.json() == {
        "detail": [{
            "loc": [
                "body",
                "prompt"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }]
    }
    assert response.is_error


@patch("src.services.v1.images_service.ImageFromAIService.generate_image")
def test_generate_image_from_openai_empty_argument(
    mock_service, client, json_header
):
    mock_service.side_effect = OpenAIApiRateLimitExceeded(exception_message)
    response = client.post(
        "/v1/generate-img-from-ai/",
        headers=json_header,
        json={"prompt": ""}
    )

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "prompt"
                ],
                "msg": "Try with a longer prompt",
                "type": "value_error"
            }
        ]
    }
    assert response.is_error


@patch("src.services.v1.images_service.ImageFromAIService.generate_image")
def test_generate_image_from_openai_exception(
    mock_service, client, json_header, prompt_payload_dict
):
    mock_service.side_effect = Exception(exception_message)
    response = client.post(
        "/v1/generate-img-from-ai/",
        headers=json_header,
        json=prompt_payload_dict
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": {"Error": f"Error at image generation: {exception_message}"}
    }
    assert response.is_error
