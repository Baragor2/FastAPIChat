from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.entities.messages import Chat


@dataclass
class BaseChatRepository(ABC):
    @abstractmethod
    def check_chat_exists_by_title(self, title: str) -> bool:
        ...


@dataclass
class MemoryChatRepository(ABC):
    _saved_chats: list[Chat]