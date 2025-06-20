from typing import Any

from .abc import AbstractStorage
from .exceptions import AddItemStorageError, GetItemStorageError


class InMemoryStorage(AbstractStorage[str, Any]):
    def __init__(self, data: dict[str, Any] | None = None) -> None:
        if data is None:
            self._data = dict()
        else:
            self._data = data

    def get(self, key: str, failed: bool = False) -> Any:
        if failed and key not in self._data:
            raise GetItemStorageError(f"Have not item with {key=}")
        return self._data.get(key)

    def add(self, key: str, value: Any, failed: bool = False) -> None:
        if failed and key in self._data:
            raise AddItemStorageError(f"Item with {key=} already exist")
        self._data[key] = value

    def have(self, value: Any) -> bool:
        return value in self._data.values()

    def clear(self) -> None:
        self._data.clear()
