import random

from pydantic import EmailStr

from auth.key_storages.abc import AbstractAuthKeyStorage
from db.types import AsyncDBSession


# TODO: account checking
async def has_account(email: EmailStr, db_session: AsyncDBSession) -> bool:
    ...


def generate_new_auth_code(storage: AbstractAuthKeyStorage) -> int:
    while True:
        code = random.randint(100_000, 1_000_000)
        return code


def auth_code(key: str, storage: AbstractAuthKeyStorage) -> int:
    code = generate_new_auth_code(storage=storage)
    storage.add(id=key, value=code)
    return code


def code_available(code: int, key: str, storage: AbstractAuthKeyStorage) -> bool:
    return storage.exist(id=key, value=code)
