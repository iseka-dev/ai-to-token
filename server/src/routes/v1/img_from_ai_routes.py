from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import HTMLResponse

from src.core.logger import log
from src.schemas.v1.schemas import PromptRequest
from src.services.v1.images_service import ImageFromAIService

generate_img_from_ai_routes = APIRouter(
    prefix="/v1/generate-img-from-ai",
    tags=["generate-img-from-ai"]
)


@generate_img_from_ai_routes.post("/", response_class=HTMLResponse)
async def generate_image_from_openai(data: PromptRequest, request: Request):
    try:
        return await ImageFromAIService().get_image(data, request)
    except Exception as e:
        log.error(f"generate_image_from_openai-E01: {e}")
        error = f"Error at img generation: {e}"
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"Error": error},
    )
