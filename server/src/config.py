import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    load_dotenv()

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "NO-API-KEY")

    CONTRACT_ADDRESS = "0xd9145CCE52D386f254917e481eB44e9943F39138"


settings = Settings()
