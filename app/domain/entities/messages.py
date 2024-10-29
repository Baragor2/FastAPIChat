from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.values.messages import Text, Title


@dataclass
class Message(BaseEntity):
    text: Text

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: 'BaseEntity') -> bool:
        return self.oid == __value.oid


@dataclass
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )

    def add_message(self, message: Message):
        self.messages.add(message)

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: 'BaseEntity') -> bool:
        return self.oid == __value.oid

