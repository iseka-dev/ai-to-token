import requests

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.settings import settings
from src.routes.v1.base_routes import router


app = FastAPI()

app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")
