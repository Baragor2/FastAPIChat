from dataclasses import dataclass

from domain.entities.messages import Chat
from domain.events.base import BaseCommand
from domain.values.messages import Title
from infra.repositories.messages import BaseChatRepository
from logic.commands.base import CommandHandler
from logic.exceptions.messages import ChatWithThatTitleAlreadyExistsException


@dataclass
class CreateChatCommand(BaseCommand):
    title: str


class CreateChatCommandHandler(CommandHandler[CreateChatCommand]):
    chat_repository: BaseChatRepository

    def handle(self, command: CreateChatCommand) -> Chat:
        if self.chat_repository.check_chat_exists_by_title(command.title):
            raise ChatWithThatTitleAlreadyExistsException(command.title)
        
        title = Title(value=command.title)
