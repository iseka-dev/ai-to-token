from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates


home_routes = APIRouter(
    prefix="",
    tags=["home"]
)

templates = Jinja2Templates(directory="templates")

@home_routes.get("/")
async def home_html(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
