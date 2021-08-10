import abc
from abc import abstractmethod
from returns.context import ReaderFutureResult as ReaderFutureResult
from returns.interfaces.specific import future_result as future_result, reader as reader, reader_ioresult as reader_ioresult
from returns.primitives.hkt import KindN as KindN
from returns.primitives.laws import LawSpecDef as LawSpecDef, Lawful as Lawful
from typing import Any, Awaitable, Callable, Type

class ReaderFutureResultLikeN(reader_ioresult.ReaderIOResultLikeN[_FirstType, _SecondType, _ThirdType], future_result.FutureResultLikeN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta):
    @abstractmethod
    def bind_context_future_result(self, function: Callable[[_FirstType], ReaderFutureResult[_UpdatedType, _SecondType, _ThirdType]]) -> KindN[_ReaderFutureResultLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @abstractmethod
    def bind_async_context_future_result(self, function: Callable[[_FirstType], Awaitable[ReaderFutureResult[_UpdatedType, _SecondType, _ThirdType]]]) -> KindN[_ReaderFutureResultLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @classmethod
    @abstractmethod
    def from_future_result_context(cls: Type[_ReaderFutureResultLikeType], inner_value: ReaderFutureResult[_ValueType, _ErrorType, _EnvType]) -> KindN[_ReaderFutureResultLikeType, _ValueType, _ErrorType, _EnvType]: ...

ReaderFutureResultLike3: Any

class _LawSpec(LawSpecDef):
    def asking_law(container: ReaderFutureResultBasedN[_FirstType, _SecondType, _ThirdType], env: _ThirdType) -> None: ...

class ReaderFutureResultBasedN(ReaderFutureResultLikeN[_FirstType, _SecondType, _ThirdType], reader.CallableReader3[_FirstType, _SecondType, _ThirdType, 'FutureResult[_FirstType, _SecondType]', _ThirdType], Lawful['ReaderFutureResultBasedN[_FirstType, _SecondType, _ThirdType]'], metaclass=abc.ABCMeta): ...

ReaderFutureResultBased3: Any
