from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class CreateUser(BaseModel):
    email: EmailStr
    account_type: Literal["private", "public"]
    username: str = Field(min_length=3, max_length=10)


class LoginUser(BaseModel):
    email: EmailStr


class AuthUser(BaseModel):
    email: EmailStr
    code: int
