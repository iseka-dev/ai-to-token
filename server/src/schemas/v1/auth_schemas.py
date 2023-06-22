from pydantic import BaseModel, Field


class LoginSchema(BaseModel):
    eth_address: str = Field(..., min_length=20)

    class Config:
        schema_extra = {
            "example": {
                "eth_address": "",
            }
        }
