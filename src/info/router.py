from fastapi import APIRouter, Request

from info import constants as info_constants
from info import utils as info_utils
from utils import template


router = APIRouter()


@router.get("/", tags=["Info Page"])
def index(request: Request):
    project_description = info_utils.project_description()
    return template(
        request,
        info_constants.HOMEPAGE,
        {
            "project_description": project_description,
        }
    )
