from config import main_config
import constants as database_constants
from db import exceptions as database_exceptions


def database_url() -> str:
    match main_config.RUNTYPE.lower():
        case database_constants.Runtypes.PRODUCTION:
            return main_config.DB_URL
        case database_constants.Runtypes.DEVELOPMENT:
            return main_config.DEV_DB_URL
    raise database_exceptions.UncorrectRuntypeEnviromient()


def database_echo() -> bool:
    return main_config.DB_ECHO
