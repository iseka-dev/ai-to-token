from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str

    class Config:
        schema_extra = {
            "example": {
                "prompt": "Draw a lot of kitty kittens",
            }
        }
