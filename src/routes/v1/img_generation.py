import requests

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi.templating import Jinja2Templates

from src.settings import settings


templates = Jinja2Templates(directory="templates")

img_generation_routes = APIRouter(
    prefix="/generate-img",
    tags=["generate_image"]
)

@img_generation_routes.post("/")
async def generate_openai_image(request: Request):
    try:
        # Get the user's input
        json_request = await request.json()
        input = json_request['input']
#   
        # Set up the POST request
        url = "https://api.openai.com/v1/images/generations"
#
        # set the request headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
        }
        # set the data for the openai API
        data = {
            'prompt': input,
            'n': 1,
            'size': '256x256'
        }
#
        # Send the request and handle the response
        try:
            response = requests.post(url, headers=headers, json=data)
        except HTTPException as e:
            raise e
        json_response = response.json()
        print(json_response)
        img_url = json_response['data'][0]['url']
        print(img_url)

        return templates.TemplateResponse(
            "image.html", {"request": request, "img_url": img_url}
        )

    except Exception as e:

        print(e)

        # log.error(f"generate_openai_image-E01: {e}")

        return e
