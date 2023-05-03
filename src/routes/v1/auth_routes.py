from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from src.core.logger import log
from src.exceptions import InvalidCredentialsException
from src.schemas.v1.auth_schemas import LoginSchema
from src.services.v1.auth_service import AuthService


auth_routes = APIRouter(
    prefix="v1/auth/",
    tags=["auth"]
)


@auth_routes.post("/login", status_code=status.HTTP_200_OK)
async def login(data: LoginSchema):
    try:
        return await AuthService().login(data)
    except InvalidCredentialsException as e:
        code = status.HTTP_401_UNAUTHORIZED
        error = f"error_auth: {e}"
    except Exception as e:
        log.error(f"error_auth: {e}")
        code = status.HTTP_400_BAD_REQUEST
        error = "Error: Login failed."
    raise HTTPException(
        status_code=code,
        detail={"error": error},
    )


# @auth_routes.post("/refresh-token", status_code=status.HTTP_200_OK)
# async def refresh_token(refresh_token: str):
#    try:
#        return await AuthService().refresh_token(refresh_token)
#    except TokenTypeException as e:
#        error = f"[RARTE01]: {e}"
#    except ExpiredSignatureError:
#        error = "[RARTE02]: Session expired, please login again."
#    except JWTError:
#        error = "[RARTE03]: Invalid token signature, please login again."
#    except Exception as e:
#        log.error(f"[RARTE04]: {e}")
#        error = "[RARTE04]: Invalid token, please login again."
#    raise HTTPException(
#        status_code=status.HTTP_401_UNAUTHORIZED,
#        detail={"error": error},
#    )
