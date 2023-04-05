import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    load_dotenv()
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "NO-API-KEY")

settings = Settings()