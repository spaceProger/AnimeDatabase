from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from src.info import constants


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", tags=["Info Page"])
def index(request: Request):
    return templates.TemplateResponse(
        constants.HOMEPAGE,
        {
            "request": request,
        }
    )
