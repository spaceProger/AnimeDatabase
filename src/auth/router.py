from fastapi import APIRouter
from fastapi import Request

from auth import constants as auth_constants
from utils import template


router = APIRouter(
    tags=[auth_constants.ROUTER_TAG],
)


@router.get("/login")
def login_page(request: Request):
    return template(request, auth_constants.LOGIN_PAGE)


@router.get("/signup")
def signup_page(request: Request):
    return template(request, auth_constants.SIGNUP_PAGE)
