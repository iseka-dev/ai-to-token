import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    load_dotenv()

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "NO-API-KEY")
    STATIC_FILES_DIRECTORY = os.getenv(
        "STATIC_FILES_DIRECTORY", "./client/static"
    )
    TEMPLATES_DIRECTORY = os.getenv(
        "TEMPLATES_DIRECTORY", "./client/templates"
    )


settings = Settings()
