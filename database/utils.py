from src.config import main_config

from database import exceptions as database_exceptions


def database_url() -> str:
    match main_config.RUNTYPE.lower():
        case "prodaction":
            return main_config.DB_URL
        case "development":
            return main_config.DEV_DB_URL
    raise database_exceptions.UncorrectRuntypeEnviromient()


def database_echo() -> bool:
    return main_config.DB_ECHO
