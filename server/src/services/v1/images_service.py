import requests
from fastapi import Request

from src.config import settings
from src.core.utils import templates
from src.schemas.v1.schemas import PromptRequest


class ImageFromAIService:
    url_open_ai = "https://api.openai.com/v1/images/generations"
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
    }

    async def get_image(self, prompt_data: PromptRequest, request: Request):
        # Create data for openai requests
        data = {
            "prompt": prompt_data.get("prompt", "no_prompt"),
            "n": 1,
            "size": "256x256"
        }

        # Send the request and handle the response
        img_url = requests.post(
            url=self.url_open_ai, headers=self.headers, json=data
        ).json()["data"][0]["url"]

        return templates.TemplateResponse(
            "image.html",
            {
                "request": request,
                "img_url": img_url,
            }
        )
