from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi import status

from src.core.logger import log
from src.services.v1.images_service import ImageGeneratorService


img_generation_routes = APIRouter(
    prefix="/generate-img",
    tags=["generate_image"]
)


@img_generation_routes.post("/")
async def generate_openai_image(request: Request):
    try:
        return await ImageGeneratorService().generate_image(request)
    except Exception as e:
        log.error(f"generate_openai_image-E01: {e}")
        error = ["Error at img generation"]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"Error": error},
    )
