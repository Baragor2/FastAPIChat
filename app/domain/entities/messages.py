from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.events.messages import NewMessageRecievedEvent
from domain.values.messages import Text, Title


@dataclass
class Message(BaseEntity):
    text: Text

    __hash__ = BaseEntity.__hash__


@dataclass(eq=False)
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )

    def add_message(self, message: Message) -> None:
        self.messages.add(message)
        self.register_event(NewMessageRecievedEvent(
            message_text=message.text.as_generic_type(),
            chat_oid=self.oid,
            message_oid=message.oid,
        ))

    __hash__ = BaseEntity.__hash__
