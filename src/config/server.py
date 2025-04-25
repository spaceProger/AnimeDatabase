from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class ServerConfig(BaseSettings):
    APP_HOST: str
    APP_PORT: int
    APP_WORKERS: int
