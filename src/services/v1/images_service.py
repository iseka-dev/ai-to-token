from abc import ABC
from abc import abstractmethod
import requests

from fastapi import Request
from fastapi.templating import Jinja2Templates

from src.settings import settings


templates = Jinja2Templates(directory="templates")


class ImageGeneratorInterface(ABC):

    @abstractmethod
    def generate_image():
        pass


class DallEImageGeneratorService(ImageGeneratorInterface):
    def generate_image():
        pass


class ImageGeneratorService:
    url = "https://api.openai.com/v1/images/generations"
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
        }

    async def generate_image(self, request: Request):
        # Get the user's input
        json_request = await request.json()
        input = json_request['input']
        data = {
            'prompt': input,
            'n': 1,
            'size': '256x256'
        }

        # Send the request and handle the response
        response = requests.post(
            url=self.url, headers=self.headers, json=data
        )
        json_response = response.json()
        img_url = json_response['data'][0]['url']

        return templates.TemplateResponse(
            "image.html", {"request": request, "img_url": img_url}
        )
