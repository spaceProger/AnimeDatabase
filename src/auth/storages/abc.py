from abc import ABC, abstractmethod


class AbstractStorage[KeyType, ValueType](ABC):
    @abstractmethod
    def get(
            self,
            key: KeyType,
            failed: bool = False,
            ) -> ValueType:
        raise NotImplementedError

    @abstractmethod
    def add(
            self,
            key: KeyType,
            value: ValueType,
            failed: bool = False,
            ) -> None:
        raise NotImplementedError

    @abstractmethod
    def have(self, value: ValueType) -> bool:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError
