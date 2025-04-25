from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from config.db import DatabaseConfig
from config.server import ServerConfig


class MainConfig(
        DatabaseConfig,
        ServerConfig,
        BaseSettings
        ):
    PROJECT_NAME: str = "anime-database"

    RUNTYPE: str

    model_config = SettingsConfigDict(
            env_file=".env",
            env_file_encoding="utf-8",
    )


main_config = MainConfig()

