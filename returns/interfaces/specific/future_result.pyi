import abc
from abc import abstractmethod
from returns.future import Future as Future, FutureResult as FutureResult
from returns.interfaces.specific import future as future, ioresult as ioresult
from returns.primitives.hkt import KindN as KindN
from typing import Any, Awaitable, Callable, Type

class FutureResultLikeN(future.FutureLikeN[_FirstType, _SecondType, _ThirdType], ioresult.IOResultLikeN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta):
    @abstractmethod
    def bind_future_result(self, function: Callable[[_FirstType], FutureResult[_UpdatedType, _SecondType]]) -> KindN[_FutureResultLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @abstractmethod
    def bind_async_future_result(self, function: Callable[[_FirstType], Awaitable[FutureResult[_UpdatedType, _SecondType]]]) -> KindN[_FutureResultLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @classmethod
    @abstractmethod
    def from_failed_future(cls: Type[_FutureResultLikeType], inner_value: Future[_ErrorType]) -> KindN[_FutureResultLikeType, _FirstType, _ErrorType, _ThirdType]: ...
    @classmethod
    def from_future_result(cls: Type[_FutureResultLikeType], inner_value: FutureResult[_ValueType, _ErrorType]) -> KindN[_FutureResultLikeType, _ValueType, _ErrorType, _ThirdType]: ...

FutureResultLike2: Any
FutureResultLike3: Any

class FutureResultBasedN(future.FutureBasedN[_FirstType, _SecondType, _ThirdType], FutureResultLikeN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta): ...

FutureResultBased2: Any
FutureResultBased3: Any
