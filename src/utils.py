from src.config import main_config


def app_host() -> str:
    return main_config.APP_HOST


def app_port() -> int:
    return main_config.APP_PORT


def app_workers() -> int:
    return main_config.APP_WORKERS
