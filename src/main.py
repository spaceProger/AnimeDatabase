from fastapi import FastAPI

from src.routers import include_routers


app = FastAPI()

include_routers(app)
