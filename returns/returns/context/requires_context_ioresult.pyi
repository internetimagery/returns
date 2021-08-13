from returns.context import NoDeps as NoDeps
from returns.context.requires_context import RequiresContext as RequiresContext
from returns.context.requires_context_result import RequiresContextResult as RequiresContextResult
from returns.interfaces.specific import reader_ioresult as reader_ioresult
from returns.io import IO as IO, IOResult as IOResult
from returns.primitives.container import BaseContainer as BaseContainer
from returns.primitives.hkt import Kind3 as Kind3, SupportsKind3 as SupportsKind3
from returns.result import Result as Result
from typing import Any, Callable, ClassVar

class RequiresContextIOResult(BaseContainer, SupportsKind3['RequiresContextIOResult', _ValueType, _ErrorType, _EnvType], reader_ioresult.ReaderIOResultBasedN[_ValueType, _ErrorType, _EnvType]):
    no_args: ClassVar[NoDeps] = ...
    def __init__(self, inner_value: Callable[[_EnvType], IOResult[_ValueType, _ErrorType]]) -> None: ...
    def __call__(self, deps: _EnvType) -> IOResult[_ValueType, _ErrorType]: ...
    def swap(self) -> RequiresContextIOResult[_ErrorType, _ValueType, _EnvType]: ...
    def map(self, function: Callable[[_ValueType], _NewValueType]) -> RequiresContextIOResult[_NewValueType, _ErrorType, _EnvType]: ...
    def apply(self, container: Kind3[RequiresContextIOResult, Callable[[_ValueType], _NewValueType], _ErrorType, _EnvType]) -> RequiresContextIOResult[_NewValueType, _ErrorType, _EnvType]: ...
    def bind(self, function: Callable[[_ValueType], Kind3[RequiresContextIOResult, _NewValueType, _ErrorType, _EnvType]]) -> RequiresContextIOResult[_NewValueType, _ErrorType, _EnvType]: ...
    bind_context_ioresult: Any = ...
    def bind_result(self, function: Callable[[_ValueType], Result[_NewValueType, _ErrorType]]) -> RequiresContextIOResult[_NewValueType, _ErrorType, _EnvType]: ...
    def bind_context(self, function: Callable[[_ValueType], RequiresContext[_NewValueType, _EnvType]]) -> RequiresContextIOResult[_NewValueType, _ErrorType, _EnvType]: ...
    def bind_context_result(self, function: Callable[[_ValueType], RequiresContextResult[_NewValueType, _ErrorType, _EnvType]]) -> RequiresContextIOResult[_NewValueType, _ErrorType, _EnvType]: ...
    def bind_io(self, function: Callable[[_ValueType], IO[_NewValueType]]) -> RequiresContextIOResult[_NewValueType, _ErrorType, _EnvType]: ...
    def bind_ioresult(self, function: Callable[[_ValueType], IOResult[_NewValueType, _ErrorType]]) -> RequiresContextIOResult[_NewValueType, _ErrorType, _EnvType]: ...
    def alt(self, function: Callable[[_ErrorType], _NewErrorType]) -> RequiresContextIOResult[_ValueType, _NewErrorType, _EnvType]: ...
    def lash(self, function: Callable[[_ErrorType], Kind3[RequiresContextIOResult, _ValueType, _NewErrorType, _EnvType]]) -> RequiresContextIOResult[_ValueType, _NewErrorType, _EnvType]: ...
    def compose_result(self, function: Callable[[Result[_ValueType, _ErrorType]], Kind3[RequiresContextIOResult, _NewValueType, _ErrorType, _EnvType]]) -> RequiresContextIOResult[_NewValueType, _ErrorType, _EnvType]: ...
    def modify_env(self, function: Callable[[_NewEnvType], _EnvType]) -> RequiresContextIOResult[_ValueType, _ErrorType, _NewEnvType]: ...
    @classmethod
    def ask(cls: Any) -> RequiresContextIOResult[_EnvType, _ErrorType, _EnvType]: ...
    @classmethod
    def from_result(cls: Any, inner_value: Result[_NewValueType, _NewErrorType]) -> RequiresContextIOResult[_NewValueType, _NewErrorType, NoDeps]: ...
    @classmethod
    def from_io(cls: Any, inner_value: IO[_NewValueType]) -> RequiresContextIOResult[_NewValueType, Any, NoDeps]: ...
    @classmethod
    def from_failed_io(cls: Any, inner_value: IO[_NewErrorType]) -> RequiresContextIOResult[Any, _NewErrorType, NoDeps]: ...
    @classmethod
    def from_ioresult(cls: Any, inner_value: IOResult[_NewValueType, _NewErrorType]) -> RequiresContextIOResult[_NewValueType, _NewErrorType, NoDeps]: ...
    @classmethod
    def from_ioresult_context(cls: Any, inner_value: ReaderIOResult[_NewValueType, _NewErrorType, _NewEnvType]) -> ReaderIOResult[_NewValueType, _NewErrorType, _NewEnvType]: ...
    @classmethod
    def from_typecast(cls: Any, inner_value: RequiresContext[IOResult[_NewValueType, _NewErrorType], _EnvType]) -> RequiresContextIOResult[_NewValueType, _NewErrorType, _EnvType]: ...
    @classmethod
    def from_context(cls: Any, inner_value: RequiresContext[_NewValueType, _NewEnvType]) -> RequiresContextIOResult[_NewValueType, Any, _NewEnvType]: ...
    @classmethod
    def from_failed_context(cls: Any, inner_value: RequiresContext[_NewValueType, _NewEnvType]) -> RequiresContextIOResult[Any, _NewValueType, _NewEnvType]: ...
    @classmethod
    def from_result_context(cls: Any, inner_value: RequiresContextResult[_NewValueType, _NewErrorType, _NewEnvType]) -> RequiresContextIOResult[_NewValueType, _NewErrorType, _NewEnvType]: ...
    @classmethod
    def from_value(cls: Any, inner_value: _NewValueType) -> RequiresContextIOResult[_NewValueType, Any, NoDeps]: ...
    @classmethod
    def from_failure(cls: Any, inner_value: _NewErrorType) -> RequiresContextIOResult[Any, _NewErrorType, NoDeps]: ...

RequiresContextIOResultE: Any
ReaderIOResult = RequiresContextIOResult
ReaderIOResultE: Any