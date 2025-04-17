from fastapi import FastAPI

import uvicorn

import utils as app_utils
from setup import setup as setup_app


app = FastAPI()
setup_app(app)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=app_utils.app_host(),
        port=app_utils.app_port(),
        workers=app_utils.app_workers(),
    )
