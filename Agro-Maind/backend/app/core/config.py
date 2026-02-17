from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Agro Maind"
    api_key: str
    database_url: str
    secret_key: str
    allowed_hosts: list = []

    class Config:
        env_file = ".env"

settings = Settings()