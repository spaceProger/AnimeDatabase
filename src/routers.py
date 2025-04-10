from fastapi import FastAPI

from src.info.router import router as info_router


def include_routers(app: FastAPI):
    app.include_router(info_router)
