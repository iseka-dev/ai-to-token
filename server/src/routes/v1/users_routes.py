from fastapi import APIRouter
# from fastapi import HTTPException
# from fastapi import status
#
# from src.core.logger import log
# from src.core.utils import templates

user_routes = APIRouter(
    prefix="/v1/users/",
    tags=["home"]
)


# @user_routes.post("/")
# async def create(request: UserRequestSchema):
#     try:
#         return templates.TemplateResponse("home.html", {"request": request})
#     except Exception as e:
#         log.error(f"Route Error: {e}")
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail={"error_home": "Home site not available"}
#     )
