from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    redis_url: str
    calendar_api_url: str
    webhook_secret: str

settings = Settings()
