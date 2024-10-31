from dataclasses import dataclass

from domain.events.base import BaseCommand


@dataclass
class NewMessageRecievedEvent(BaseCommand):
    message_text: str
    message_oid: str
    chat_oid: str
