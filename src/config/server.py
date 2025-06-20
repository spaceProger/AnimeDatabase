from pydantic_settings import BaseSettings


class ServerConfig(BaseSettings):
    APP_HOST: str
    APP_PORT: int
    APP_WORKERS: int
