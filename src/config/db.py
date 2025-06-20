from pydantic import FilePath
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    DB_USER: str
    DB_NAME: str
    DB_ECHO: bool
    DB_HOST: str
    DB_PORT: int
    DB_PASSWORD: str

    DEV_DB_FILEPATH: FilePath

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@\
                {self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DEV_DB_URL(self) -> str:
        return f"sqlite+aiosqlite:///{self.DEV_DB_FILEPATH}"
