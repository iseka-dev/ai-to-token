import requests
from fastapi import Request

from src.config import settings
from src.core.logger import log
from src.core.utils import templates
from src.exceptions import OpenAIApiRateLimitExceeded
from src.schemas.v1.schemas import PromptRequest


class ImageFromAIService:
    """
    Class to get images from OPEN AI
    """
    url_open_ai = "https://api.openai.com/v1/images/generations"
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
    }

    async def generate_image(
        self, data: PromptRequest, request: Request
    ) -> templates.TemplateResponse:

        # Create data for openai requests
        new_data = {
            "prompt": data.prompt,
            "n": 10,
            "size": "256x256"
        }

        log.info("Querying third party api...")

        # Send the request and handle the response
        json_response = requests.post(
            url=self.url_open_ai, headers=self.headers, json=new_data
        ).json()

        log.debug(json_response)

        try:
            img_url = json_response["data"][0]["url"]
        except KeyError as e:
            if json_response["error"]["code"] == "rate_limit_exceeded":
                raise OpenAIApiRateLimitExceeded(
                    "OpenAI API rate limit exceeded"
                ) from e

        return templates.TemplateResponse(
            "image.html",
            {
                "request": request,
                "img_url": img_url,
            }
        )
