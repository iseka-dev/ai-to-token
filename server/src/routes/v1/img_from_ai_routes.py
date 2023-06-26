from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import HTMLResponse

from src.core.logger import log
from src.services.v1.images_service import ImageFromAIService

generate_img_from_ai_routes = APIRouter(
    prefix="/v1/generate-img-from-ai",
    tags=["generate_image"]
)


@generate_img_from_ai_routes.post("/", response_class=HTMLResponse)
async def generate_image_from_openai(request: Request):
    try:
        return await ImageFromAIService().get_image(request)
    except Exception as e:
        log.error(f"get_image_from_openai-E01: {e}")
        error = f"Error at img generation: {e}"
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"Error": error},
    )
