import abc
from abc import abstractmethod
from returns.interfaces.specific import io as io, result as result
from returns.io import IO as IO, IOResult as IOResult
from returns.primitives.hkt import KindN as KindN
from returns.result import Result as Result
from typing import Any, Callable, Type

class IOResultLikeN(io.IOLikeN[_FirstType, _SecondType, _ThirdType], result.ResultLikeN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta):
    @abstractmethod
    def bind_ioresult(self, function: Callable[[_FirstType], IOResult[_UpdatedType, _SecondType]]) -> KindN[_IOResultLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @abstractmethod
    def compose_result(self, function: Callable[[Result[_FirstType, _SecondType]], KindN[_IOResultLikeType, _UpdatedType, _SecondType, _ThirdType]]) -> KindN[_IOResultLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @classmethod
    @abstractmethod
    def from_ioresult(cls: Type[_IOResultLikeType], inner_value: IOResult[_ValueType, _ErrorType]) -> KindN[_IOResultLikeType, _ValueType, _ErrorType, _ThirdType]: ...
    @classmethod
    @abstractmethod
    def from_failed_io(cls: Type[_IOResultLikeType], inner_value: IO[_ErrorType]) -> KindN[_IOResultLikeType, _FirstType, _ErrorType, _ThirdType]: ...

IOResultLike2: Any
IOResultLike3: Any

class IOResultBasedN(IOResultLikeN[_FirstType, _SecondType, _ThirdType], io.IOBasedN[_FirstType, _SecondType, _ThirdType], result.UnwrappableResult[_FirstType, _SecondType, _ThirdType, 'IO[_FirstType]', 'IO[_SecondType]'], metaclass=abc.ABCMeta): ...

IOResultBased2: Any
IOResultBased3: Any
