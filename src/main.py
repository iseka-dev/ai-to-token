from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings

from .settings import settings

import requests

from src.core.logger import log

class Settings(BaseSettings):
    OPENAI_API_KEY: str = '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'

app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home_html(request: Request):
    return templates.TemplateResponse("home.html", {"request":request})

@app.post("/generate-image")
async def generate_openai_image(request: Request):
    try:
        # Get the user's input
        json_request = await request.json()
        input = json_request['input']

        # Set up the POST request
        url = "https://api.openai.com/v1/images/generations"

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

        # Send the request and handle the response
        response = requests.post(url, headers=headers, json=data)
        json_response = response.json()
        img_url = json_response['data'][0]['url']

        #img_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-eaP1VvwvM1IlT9JCcAifBo0I/user-kPAWi7e8GvLvcJGxUQaIbzmZ/img-pA5KarGtjqyrcKRUpCH2t8kI.png?st=2023-04-05T15%3A21%3A05Z&se=2023-04-05T17%3A21%3A05Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-05T15%3A42%3A11Z&ske=2023-04-06T15%3A42%3A11Z&sks=b&skv=2021-08-06&sig=RHgU1gM4HuGGPOXsA9mPxEQ47Lor6skkB2sw7mKw9ww%3D"

        return { 'img_url': img_url }

    except Exception as e:

        print(e)

        # log.error(f"generate_openai_image-E01: {e}")

        return e
