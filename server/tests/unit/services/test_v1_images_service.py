import pytest
from mock import Mock, patch

from src.exceptions import OpenAIApiRateLimitExceeded
from src.services.v1.images_service import ImageFromAIService


@pytest.mark.asyncio
@patch("requests.post")
async def test_get_image_from_ai_generate_image_success(
    mocked_post, prompt_payload_schema
):
    mocked_post.return_value = Mock(
        status_code=200, json=lambda: {
            "data": [
                {"url": "some_url"}
            ]
        }
    )

    response = await ImageFromAIService().generate_image(
        prompt_payload_schema, {}
    )

    assert response.status_code == 200
    assert response.template.name == "image.html"
    assert "request" in response.context
    assert "img_url" in response.context


@pytest.mark.asyncio
async def test_get_image_from_ai_rate_limit_exceeded_exception(
    prompt_payload_schema
):
    with pytest.raises(OpenAIApiRateLimitExceeded) as e:
        await ImageFromAIService().generate_image(prompt_payload_schema, {})

    assert str(e.value) == "OpenAI API rate limit exceeded"
