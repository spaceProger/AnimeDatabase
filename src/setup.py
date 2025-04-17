from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from info.router import router as info_router


def include_routers(app: FastAPI) -> None:
    app.include_router(info_router)


def mount_files(app: FastAPI) -> None:
    app.mount('/static', StaticFiles(directory="templates"), name="static")


def setup(app: FastAPI) -> None:
    include_routers(app)
    mount_files(app)
