from abc import ABC
from abc import abstractmethod
import requests

from fastapi import Request

from src.core.logger import log
from src.settings import settings
from src.core.utils import templates


class ImageGeneratorInterface(ABC):

    @abstractmethod
    def generate_image():
        pass


class DallEImageGeneratorService(ImageGeneratorInterface):
    def generate_image():
        pass


class ImageGeneratorService:
    url_open_ai = "https://api.openai.com/v1/images/generations"
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
    }

    async def generate_image(
        self, request: Request
    ):
        # Get the user's input
        json_request = await request.json()
        # log.debug("****************", type(json_request))
        input = json_request['input']
        data = {
            'prompt': input,
            'n': 1,
            'size': '256x256'
        }

        log.error(json_request)

        log.error(input)

        # Send the request and handle the response
        json_response = requests.post(
            url=self.url_open_ai, headers=self.headers, json=data
        ).json()
        log.error(json_response)
        img_url = json_response['data'][0]['url']
        log.error(img_url)

        return templates.TemplateResponse(
            "image.html", {"request": request, "img_url": img_url}
        )
