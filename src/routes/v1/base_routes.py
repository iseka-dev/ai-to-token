from fastapi import APIRouter
from src.routes.v1.home_routes import home_routes
from src.routes.v1.img_generation import img_generation_routes


router = APIRouter()

router.include_router(home_routes)
router.include_router(img_generation_routes)
