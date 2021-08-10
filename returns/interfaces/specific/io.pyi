import abc
from abc import abstractmethod
from returns.interfaces import container as container, equable as equable
from returns.io import IO as IO
from returns.primitives.hkt import KindN as KindN
from typing import Any, Callable, Type

class IOLikeN(container.ContainerN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta):
    @abstractmethod
    def bind_io(self, function: Callable[[_FirstType], IO[_UpdatedType]]) -> KindN[_IOLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @classmethod
    @abstractmethod
    def from_io(cls: Type[_IOLikeType], inner_value: IO[_UpdatedType]) -> KindN[_IOLikeType, _UpdatedType, _SecondType, _ThirdType]: ...

IOLike1: Any
IOLike2: Any
IOLike3: Any

class IOBasedN(IOLikeN[_FirstType, _SecondType, _ThirdType], equable.Equable, metaclass=abc.ABCMeta): ...

IOBased1: Any
IOBased2: Any
IOBased3: Any
