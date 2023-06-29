from fastapi import APIRouter, HTTPException, Request, status

from src.core.logger import log
from src.core.utils import templates

index_routes = APIRouter(
    prefix="",
    tags=["home"]
)


@index_routes.get("/")
async def get_index_html(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        log.error(f"Route Error: {e}")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"error_home": "Home site not available"}
    )
