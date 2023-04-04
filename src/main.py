from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings

import requests
import json

import io

from src.core.logger import log

class Settings(BaseSettings):
    OPENAI_API_KEY: str = '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'

settings = Settings()
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
            "prompt": input,
            "n": 1,
            "size": "256x256"
        }

        # Send the request and handle the response
        response = requests.post(url, headers=headers, json=data)
        json_response = response.json()
        img_url = json_response['data'][0]['url']

        return { "img_url": img_url }

    except Exception as e:

        print(e)

        # log.error(f"generate_openai_image-E01: {e}")

        return e
