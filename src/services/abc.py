from abc import ABC, abstractmethod
from datetime import datetime, timezone

from pydantic import BaseModel, Field


class Event(BaseModel):
    timestamp: datetime = Field(
            default_factory=lambda: datetime.now(timezone.utc))


class AbstractObserver[EventType](ABC):
    @abstractmethod
    def accept(self, event: EventType) -> None:
        raise NotImplementedError
