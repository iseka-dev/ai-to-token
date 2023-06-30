import pytest
from mock import Mock, patch

from src.services.v1.images_service import ImageFromAIService


@pytest.mark.asyncio
@patch("requests.post")
async def test_get_image_from_ai_get_image_success(
    mocked_post, prompt_payload
):
    mocked_post.return_value = Mock(
        status_code=200, json=lambda: {
            "data": [
                {"url": "some_url"}
            ]
        }
    )

    response = await ImageFromAIService().get_image(prompt_payload, {})

    assert response.status_code == 200
    assert response.template.name == "image.html"
    assert "request" in response.context
    assert "img_url" in response.context


@pytest.mark.asyncio
async def test_get_image_from_ai_get_image_no_prompt_input():
    response = await ImageFromAIService().get_image({}, {})

    assert response.status_code == 400
    assert "request" not in response.context
    assert "img_url" not in response.context