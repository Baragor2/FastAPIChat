from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(frozen=True, eq=False)
class EventHandlersNotRegisteredException(LogicException):
    event_type: type

    @property
    def message(self):
        return f"Handlers for event {self.event_type} not found"


@dataclass(frozen=True, eq=False)
class CommandHandlersNotRegisteredException(LogicException):
    command_type: type

    @property
    def message(self):
        return f"Handlers for command {self.command_type} not found"