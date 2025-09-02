from abc import ABC, abstractmethod


class AbstractAuthKeyStorage[KeyID, KeyValue](ABC):
    @abstractmethod
    def __init__(
            self,
            data: dict[KeyID, KeyValue] | None = None,
            **kwargs,
            ) -> None:
        raise NotImplementedError

    @abstractmethod
    def add(
            self,
            id: KeyID,
            value: KeyValue,
            **kwargs,
            ) -> None:
        raise NotImplementedError

    @abstractmethod
    def exist(
            self,
            id: KeyID,
            value: KeyValue,
            ) -> bool:
        raise NotImplementedError

    @abstractmethod
    def remove(
            self,
            id: KeyID,
            ) -> None:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError
