from abc import ABCMeta
from inspect import FrameInfo as FrameInfo
from returns.interfaces.specific import io as io, ioresult as ioresult
from returns.primitives.container import BaseContainer as BaseContainer
from returns.primitives.hkt import Kind1 as Kind1, Kind2 as Kind2, SupportsKind1 as SupportsKind1, SupportsKind2 as SupportsKind2
from returns.result import Result as Result
from typing import Any, Callable, ClassVar, List, Optional, Type, Union

class IO(BaseContainer, SupportsKind1['IO', _ValueType], io.IOLike1[_ValueType]):
    equals: Any = ...
    def __init__(self, inner_value: _ValueType) -> None: ...
    def map(self, function: Callable[[_ValueType], _NewValueType]) -> IO[_NewValueType]: ...
    def apply(self, container: Kind1[IO, Callable[[_ValueType], _NewValueType]]) -> IO[_NewValueType]: ...
    def bind(self, function: Callable[[_ValueType], Kind1[IO, _NewValueType]]) -> IO[_NewValueType]: ...
    bind_io: Any = ...
    @classmethod
    def from_value(cls: Any, inner_value: _NewValueType) -> IO[_NewValueType]: ...
    @classmethod
    def from_io(cls: Any, inner_value: IO[_NewValueType]) -> IO[_NewValueType]: ...
    @classmethod
    def from_ioresult(cls: Any, inner_value: IOResult[_NewValueType, _NewErrorType]) -> IO[Result[_NewValueType, _NewErrorType]]: ...

def impure(function: Callable[..., _NewValueType]) -> Callable[..., IO[_NewValueType]]: ...

class IOResult(BaseContainer, SupportsKind2['IOResult', _ValueType, _ErrorType], ioresult.IOResultBased2[_ValueType, _ErrorType], metaclass=ABCMeta):
    __match_args__: Any = ...
    success_type: ClassVar[Type[IOSuccess]]
    failure_type: ClassVar[Type[IOFailure]]
    equals: Any = ...
    def __init__(self, inner_value: Result[_ValueType, _ErrorType]) -> None: ...
    @property
    def trace(self) -> Optional[List[FrameInfo]]: ...
    def swap(self) -> IOResult[_ErrorType, _ValueType]: ...
    def map(self, function: Callable[[_ValueType], _NewValueType]) -> IOResult[_NewValueType, _ErrorType]: ...
    def apply(self, container: Kind2[IOResult, Callable[[_ValueType], _NewValueType], _ErrorType]) -> IOResult[_NewValueType, _ErrorType]: ...
    def bind(self, function: Callable[[_ValueType], Kind2[IOResult, _NewValueType, _ErrorType]]) -> IOResult[_NewValueType, _ErrorType]: ...
    bind_ioresult: Any = ...
    def bind_result(self, function: Callable[[_ValueType], Result[_NewValueType, _ErrorType]]) -> IOResult[_NewValueType, _ErrorType]: ...
    def bind_io(self, function: Callable[[_ValueType], IO[_NewValueType]]) -> IOResult[_NewValueType, _ErrorType]: ...
    def alt(self, function: Callable[[_ErrorType], _NewErrorType]) -> IOResult[_ValueType, _NewErrorType]: ...
    def lash(self, function: Callable[[_ErrorType], Kind2[IOResult, _ValueType, _NewErrorType]]) -> IOResult[_ValueType, _NewErrorType]: ...
    def value_or(self, default_value: _NewValueType) -> IO[Union[_ValueType, _NewValueType]]: ...
    def unwrap(self) -> IO[_ValueType]: ...
    def failure(self) -> IO[_ErrorType]: ...
    def compose_result(self, function: Callable[[Result[_ValueType, _ErrorType]], Kind2[IOResult, _NewValueType, _ErrorType]]) -> IOResult[_NewValueType, _ErrorType]: ...
    @classmethod
    def from_typecast(cls: Any, inner_value: IO[Result[_NewValueType, _NewErrorType]]) -> IOResult[_NewValueType, _NewErrorType]: ...
    @classmethod
    def from_failed_io(cls: Any, inner_value: IO[_NewErrorType]) -> IOResult[Any, _NewErrorType]: ...
    @classmethod
    def from_io(cls: Any, inner_value: IO[_NewValueType]) -> IOResult[_NewValueType, Any]: ...
    @classmethod
    def from_result(cls: Any, inner_value: Result[_NewValueType, _NewErrorType]) -> IOResult[_NewValueType, _NewErrorType]: ...
    @classmethod
    def from_ioresult(cls: Any, inner_value: IOResult[_NewValueType, _NewErrorType]) -> IOResult[_NewValueType, _NewErrorType]: ...
    @classmethod
    def from_value(cls: Any, inner_value: _NewValueType) -> IOResult[_NewValueType, Any]: ...
    @classmethod
    def from_failure(cls: Any, inner_value: _NewErrorType) -> IOResult[Any, _NewErrorType]: ...

class IOFailure(IOResult[Any, _ErrorType]):
    def __init__(self, inner_value: _ErrorType) -> None: ...

class IOSuccess(IOResult[_ValueType, Any]):
    def __init__(self, inner_value: _ValueType) -> None: ...

IOResultE: Any

def impure_safe(function: Callable[..., _NewValueType]) -> Callable[..., IOResultE[_NewValueType]]: ...