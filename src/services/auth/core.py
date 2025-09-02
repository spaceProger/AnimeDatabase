from random import randint
from typing import Unpack

from auth.key_storages import AbstractAuthKeyStorage
from services.abc import AbstractObserver
from services.auth import types as auth_types


class AuthService(object):
    def __init__(
            self,
            auth_key_storage: AbstractAuthKeyStorage,
            sign_up_observers: list[AbstractObserver[auth_types.SignUpEvent]],
            len_auth_code: int = 6,
            ) -> None:
        self.auth_key_storage = auth_key_storage
        self.sign_up_observers = sign_up_observers
        self.len_auth_code = len_auth_code

    def generate_auth_code(self) -> int:
        auth_code = randint(
                a=10 ** (self.len_auth_code - 1),
                b=10 ** self.len_auth_code - 1)
        return auth_code

    def new_auth_code(
            self,
            id: str,
            ) -> int:
        auth_code = self.generate_auth_code()
        self.auth_key_storage.add(
                id=id,
                value=auth_code,
                lifetime=30)
        return auth_code

    def sign_up_user(
            self,
            **kwargs: Unpack[auth_types.SignUpUserInput],
            ) -> None:
        email = kwargs["email"]
        auth_code = self.new_auth_code(id=email)

        new_sign_up = auth_types.SignUpEvent(user_email=email, auth_code=auth_code)

        for observer in self.sign_up_observers:
            observer.accept(new_sign_up)
