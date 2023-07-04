from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import HTMLResponse

from src.core.logger import log
from src.exceptions import OpenAIApiRateLimitExceeded
from src.schemas.v1.schemas import PromptRequest
from src.services.v1.images_service import ImageFromAIService

generate_img_from_ai_routes = APIRouter(
    prefix="/v1/generate-img-from-ai",
    tags=["generate-img-from-ai"]
)


@generate_img_from_ai_routes.post("/", response_class=HTMLResponse)
async def generate_image_from_openai(data: PromptRequest, request: Request):
    """
    Generates an image through the OpenAI API

    - **prompt_data**: Dict/Schma with a "prompt" field,
    used for image generation.
    - **request**: used for Jinja2 TemplateResponse.

    **TemplateResponse** with the generated image
    """
    try:
        return await ImageFromAIService().generate_image(data, request)
    except OpenAIApiRateLimitExceeded as e:
        log.debug(f"generate_image_from_openai-E01: {e}")
        error = f"Error at image generation: {e}"
        code = status.HTTP_429_TOO_MANY_REQUESTS
    except Exception as e:
        log.debug(f"generate_image_from_openai-E01: {e}")
        error = f"Error at image generation: {e}"
        code = status.HTTP_400_BAD_REQUEST
    raise HTTPException(
        status_code=code,
        detail={"Error": error},
    )
