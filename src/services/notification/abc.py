from abc import ABC, abstractmethod
from typing import Any


class AbstractNotificationService(ABC):
    @abstractmethod
    def send_message(
            self,
            recipient: str,
            text: str,
            **kwargs,
            ) -> Any | None:
        raise NotImplementedError
