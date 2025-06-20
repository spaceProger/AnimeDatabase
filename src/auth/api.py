from fastapi import APIRouter

from auth import constants as auth_constants
from auth import utils as auth_utils
from pydantic import EmailStr
from services.alerts import email_client


router = APIRouter(
    prefix="/api",
    tags=["Authorization"],
)


@router.post("/login")
def login(email: EmailStr):
    code = auth_utils.auth_code()
    mailbox = email_client()
    mailbox.message(
        to_email_box=email,
        text=auth_constants.LOGIN_EMAIL_MESSAGE.format(code=code),
        subject=auth_constants.LOGIN_EMAIL_SUBJECT,
    )
    return {"status": "ok", "message": "Mail was sended"}
