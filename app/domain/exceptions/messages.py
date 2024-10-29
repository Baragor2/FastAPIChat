from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass
class TitleTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f'Слишком длинный текст сообщения "{self.text[:255]}..."'


@dataclass(eq=False)
class EmptyTextException(ApplicationException):
    @property
    def message(self):
        return 'The text cannot be blank'