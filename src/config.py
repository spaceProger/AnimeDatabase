from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class DatabaseConfig(BaseSettings):
    DB_USER: str
    DB_NAME: str
    DB_ECHO: bool
    DB_HOST: str
    DB_PORT: int
    DB_PASSWORD: str

    DEV_DB_FILEPATH: str

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@\
                {self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DEV_DB_URL(self) -> str:
        return f"sqlite+aiosqlite://{self.DEV_DB_FILEPATH}"


class ServerConfig(BaseSettings):
    APP_HOST: str
    APP_PORT: int
    APP_WORKERS: int


class MainConfig(DatabaseConfig, ServerConfig, BaseSettings):
    PROJECT_NAME: str = "anime-database"

    RUNTYPE: str

    model_config = SettingsConfigDict(
            env_file=".env",
            env_file_encoding="utf-8",
    )


main_config = MainConfig()

