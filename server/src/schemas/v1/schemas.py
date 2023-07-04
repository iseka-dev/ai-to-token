from pydantic import BaseModel, validator

from src.core.logger import log


class PromptRequest(BaseModel):
    prompt: str

    @validator("prompt")
    def prompt_should_be_longer_than_three(cls, arg):
        log.debug(arg)
        log.debug(len(arg))
        if len(arg) < 3:
            raise ValueError("Try with a longer prompt")
        return arg

    class Config:
        schema_extra = {
            "example": {
                "prompt": "Draw a lot of kitty kittens",
            }
        }
