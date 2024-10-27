from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Generic, TypeVar, Any


VT = TypeVar('VT', bound=Any)


@dataclass(frozen=True)
class BaseValueObject(ABC, Generic[VT]):
    value: VT

    @abstractmethod
    def validate(self):
        ...

    @abstractmethod
    def as_generic_type(self):
        ...
