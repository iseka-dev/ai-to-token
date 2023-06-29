from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str

    class Config:
        schema_extra = {
            "example": {
                "prompt": "a random prompt to be introduced in chat GPT-3",
            }
        }
