from unittest.mock import patch


@patch("src.services.v1.images_service.ImageFromAIService.get_image")
def test_get_image_from_openai_success(
    mock_service, client, json_header, prompt_payload
):
    expected_from_service = "This is a mocked templated"
    mock_service.return_value = expected_from_service
    response = client.post(
        "/v1/generate-img-from-ai/", headers=json_header, json=prompt_payload
    )

    assert response.status_code == 200
    assert response.text == expected_from_service
    assert response.is_success


@patch("src.services.v1.images_service.ImageFromAIService.get_image")
def test_get_image_from_openai_exception(
    mock_service, client, json_header, prompt_payload
):
    exception_message = "This is an exception"
    mock_service.side_effect = Exception(exception_message)
    response = client.post(
        "/v1/generate-img-from-ai/", headers=json_header, json=prompt_payload
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": {"Error": f"Error at img generation: {exception_message}"}
    }
    assert response.is_error
