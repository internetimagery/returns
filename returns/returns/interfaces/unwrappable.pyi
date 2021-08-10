import abc
from abc import abstractmethod

class Unwrappable(metaclass=abc.ABCMeta):
    @abstractmethod
    def unwrap(self) -> _FirstType: ...
    @abstractmethod
    def failure(self) -> _SecondType: ...
