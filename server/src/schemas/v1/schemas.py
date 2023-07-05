from pydantic import BaseModel, validator


class PromptRequest(BaseModel):
    prompt: str

    @validator("prompt")
    def prompt_should_be_longer_than_three(cls, arg):
        if len(arg) < 3:
            raise ValueError("Try with a longer prompt")
        return arg

    class Config:
        schema_extra = {
            "example": {
                "prompt": "Draw a lot of kitty kittens",
            }
        }
