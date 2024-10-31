from abc import ABC
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from domain.events.base import BaseCommand


ET = TypeVar(name='ET', bound=BaseCommand)
ER = TypeVar(name='ER', bound=Any)


@dataclass
class EventHandler(ABC, Generic[ET, ER]):
    def handle(self, event: ET) -> ER:
        ...
