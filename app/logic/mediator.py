from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable

from domain.events.base import BaseCommand
from logic.commands.base import CR, CT, BaseCommand, CommandHandler
from logic.events.base import ER, ET, EventHandler
from logic.exceptions.mediator import CommandHandlersNotRegisteredException, EventHandlersNotRegisteredException


@dataclass(eq=False)
class Mediator:
    events_map: dict[ET, EventHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )
    commands_map: dict[CT, CommandHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    def register_event(self, event: ET, event_handler: EventHandler[ET, ER]):
        self.events_map[event.__class__].append(event_handler)

    def register_command(self, command: CT, command_handler: EventHandler[CT, CR]):
        self.events_map[command.__class__].append(command_handler)
    
    def handle_event(self, event: BaseCommand) -> Iterable[ER]:
        event_type = event.__class__
        handlers = self.events_map.get(event_type)

        if not handlers:
            raise EventHandlersNotRegisteredException(event_type)

        return [handler.handle(event) for handler in handlers]

    def handle_comands(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.events_map.get(command_type)

        if not handlers:
            raise CommandHandlersNotRegisteredException(command_type)

        return [handler.handle(command) for handler in handlers]