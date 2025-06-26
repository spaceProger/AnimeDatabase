from typing import Annotated, Any

from fastapi import APIRouter, Form
from fastapi.exceptions import HTTPException

from auth import constants as auth_constants
from auth import schemas as auth_schemas
from auth import utils as auth_utils
from auth.storages import InMemoryStorage
from db import async_session as async_db_session
from services.alerts import email_client


router = APIRouter(
    prefix="/api",
    tags=[auth_constants.ROUTER_TAG],
)


# TODO: add depends
@router.post("/login")
async def auth_email(
        user: Annotated[auth_schemas.LoginUser, Form()],
        ) -> dict[str, str]:
    db_session = async_db_session()
    if await auth_utils.has_account(email=user.email, db_session=db_session):
        text=auth_constants.LOGIN_EMAIL_MESSAGE
        subject=auth_constants.LOGIN_EMAIL_SUBJECT
    else:
        text=auth_constants.SIGNUP_EMAIL_MESSAGE
        subject=auth_constants.SIGNUP_EMAIL_SUBJECT
    await db_session.close()

    storage = InMemoryStorage()
    code = auth_utils.auth_code(key=user.email, storage=storage)

    mailbox = email_client()
    mailbox.message(
        to_email_box=user.email,
        text=text.format(code=code),
        subject=subject,
    )

    return {"status": "ok", "message": "Mail was sended"}


# TODO: add depends
@router.post("/auth")
def auth_code(
        user: Annotated[auth_schemas.AuthUser, Form()],
        ):
    storage = InMemoryStorage()
    if auth_utils.code_available(
            code=user.code,
            key=user.email,
            storage=storage,
            ):
        # TODO: authorization ...
        return {"status": "success", "message": "authorization passed"}
    raise HTTPException(status_code=401, detail="authorization failed")


# TODO: add depends
@router.post("/user")
def new_user(
        user: Annotated[auth_schemas.CreateUser, Form()],
        ) -> dict[str, Any]:
    # TODO: adding user to db
    #       and returning user_id
    user_id = 0
    return {
        "status": "success",
        "message": "user was created",
        "user_id": user_id,
    }
