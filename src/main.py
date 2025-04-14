from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.routers import include_routers


app = FastAPI()

app.mount('/static', StaticFiles(directory="templates"), name="static")

include_routers(app)
