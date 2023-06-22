from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config import settings
from src.routes.base_routes import router

app = FastAPI()

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(directory=settings.STATIC_FILES_DIRECTORY),
    name="static"
)
