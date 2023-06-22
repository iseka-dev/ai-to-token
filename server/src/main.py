from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.routes.base_routes import router


app = FastAPI()

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(directory="../client/static"),
    name="static"
)
