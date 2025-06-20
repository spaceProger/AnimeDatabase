import random
from typing import Any

from pydantic import EmailStr

from auth.storages.abc import AbstractStorage
from db.types import AsyncDBSession


# TODO: account checking
async def has_account(email: EmailStr, db_session: AsyncDBSession) -> bool:
    ...


def generate_new_auth_code(storage: AbstractStorage) -> int:
    while True:
        code = random.randint(100_000, 1_000_000)
        if not storage.have(value=code):
            return code


def auth_code(key: str, storage: AbstractStorage) -> int:
    code = generate_new_auth_code(storage=storage)
    storage.add(key=key, value=code)
    return code


def code_available(code: int, key: str, storage: AbstractStorage) -> bool:
    return code == storage.get(key=key)
