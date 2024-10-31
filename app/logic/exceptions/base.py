from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class LogicException(ApplicationException):
    @property
    def message(self):
        return 'An error occurred in processing the request'
