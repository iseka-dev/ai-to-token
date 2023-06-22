from fastapi import APIRouter

from src.routes.v1.index_routes import index_routes
from src.routes.v1.img_generation_routes import img_generation_routes


router = APIRouter()


@router.get("/health-check", tags=["health-check"])
async def health_check():
    return {"check": {"server": "OK", "database": "OK"}}


router.include_router(index_routes)
router.include_router(img_generation_routes)
