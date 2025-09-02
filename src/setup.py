from typing import Sequence

from fastapi import FastAPI, APIRouter, Depends
from fastapi.staticfiles import StaticFiles

from auth.api import router as auth_api
from auth.key_storages import InMemoryAuthKeyStorage
from auth.router import router as auth_router
from config import main_config as main_config
from info.router import router as info_router
from services.auth import AuthService
from services.notification import EmailNotificationService
from services.notification.sign_up_observer import SignUpNotificationObserver


def include_routers(app: FastAPI, routers: Sequence[APIRouter]) -> FastAPI:
    for router in routers:
        app.include_router(router)
    return app


def mount_files(app: FastAPI) -> FastAPI:
    app.mount(
        path='/static',
        app=StaticFiles(directory="templates/static"),
        name="static")
    return app


def setup(app: FastAPI) -> FastAPI:
    app = include_routers(
        app,
        routers=[
            auth_api,
            auth_router,
            info_router,
        ],
    )
    app = mount_files(app)
    return app


def get_app() -> FastAPI:
    notification_service = EmailNotificationService(
        domen=main_config.EMAIL_DOMEN,
        email=main_config.EMAIL_BOX,
        email_password=main_config.EMAIL_BOX_PASSWORD,
    )
    auth_service = AuthService(
            auth_key_storage=InMemoryAuthKeyStorage(),
            sign_up_observers=[
                SignUpNotificationObserver(
                    notification_service=notification_service)
                ]
            )

    app = FastAPI(dependencies=[
        Depends(lambda: notification_service),
        Depends(lambda: auth_service),
    ])
    app = setup(app=app)

    return app
