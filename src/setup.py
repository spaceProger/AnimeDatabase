from typing import Sequence

from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

from auth.api import router as auth_api
from auth.router import router as auth_router
from info.router import router as info_router


def include_routers(app: FastAPI, routers: Sequence[APIRouter]) -> None:
    for router in routers:
        app.include_router(router)


def mount_files(app: FastAPI) -> None:
    app.mount('/static', StaticFiles(directory="templates/static"), name="static")


def setup(app: FastAPI) -> None:
    include_routers(
        app,
        routers=[
            auth_api,
            auth_router,
            info_router,
        ],
    )
    mount_files(app)
