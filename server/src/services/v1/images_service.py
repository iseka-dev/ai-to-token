import requests

from fastapi import Request

from src.config import settings
from src.core.utils import templates


class ImageGeneratorService:
    url_open_ai = "https://api.openai.com/v1/images/generations"
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
    }

    async def get_image(
        self, request: Request
    ):
        # Get the user's input
        json_request = await request.json()
        prompt = json_request['input']
        data = {
            'prompt': prompt,
            'n': 1,
            'size': '256x256'
        }

        # Send the request and handle the response
        json_response = requests.post(
            url=self.url_open_ai, headers=self.headers, json=data
        ).json()
        img_url = json_response['data'][0]['url']

        return templates.TemplateResponse(
            "image.html",
            {
                "request": request,
                "img_url": img_url,
            }
        )
