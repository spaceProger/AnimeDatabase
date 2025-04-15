from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from src.info import constants as info_constants
from src.info import utils as info_utils


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", tags=["Info Page"])
def index(request: Request):
    project_description = info_utils.project_description()
    return templates.TemplateResponse(
        info_constants.HOMEPAGE,
        {
            "request": request,
            "project_description": project_description,
        }
    )
