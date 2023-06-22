from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.responses import HTMLResponse


from src.core.logger import log
from src.services.v1.images_service import ImageGeneratorService


img_generation_routes = APIRouter(
    prefix="/v1/generate-img",
    tags=["generate_image"]
)


@img_generation_routes.post("/", response_class=HTMLResponse)
async def get_image_from_openai(request: Request):
    try:
        return await ImageGeneratorService().get_image(request)
    except Exception as e:
        log.error(f"get_image_from_openai-E01: {e}")
        error = f"Error at img generation: {e}"
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"Error": error},
    )
