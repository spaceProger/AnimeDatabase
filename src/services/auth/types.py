from typing import TypedDict

from services.abc import Event


class VerifyUserInput(TypedDict):
    email: str


class SignUpUserInput(TypedDict):
    email: str


class SignUpEvent(Event):
    user_email: str
    auth_code: int
