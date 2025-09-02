from auth.key_storages.abc import AbstractAuthKeyStorage
from auth.key_storages.exceptions import AddItemStorageError


class InMemoryAuthKeyStorage(AbstractAuthKeyStorage[str, int]):
    def __init__(self, data: dict[str, int] | None = None) -> None:
        self._data: dict[str, int] = dict()
        if data is not None:
            self._data = data

    def add(
            self,
            id: str,
            value: int,
            **kwargs,
            ) -> None:
        if id in self._data:
            raise AddItemStorageError(f"Item with {id=} already exist")
        self._data[id] = value

    def exist(self, id: str, value: int) -> bool:
        return value == self._data.get(id)

    def remove(self, id: str) -> None:
        self._data.pop(id)

    def clear(self) -> None:
        self._data.clear()
