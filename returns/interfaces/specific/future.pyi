import abc
from abc import abstractmethod
from returns.future import Future as Future
from returns.interfaces.specific import io as io
from returns.primitives.hkt import KindN as KindN
from typing import Any, Awaitable, Callable, Generator, Type

class FutureLikeN(io.IOLikeN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta):
    @abstractmethod
    def bind_future(self, function: Callable[[_FirstType], Future[_UpdatedType]]) -> KindN[_FutureLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @abstractmethod
    def bind_async_future(self, function: Callable[[_FirstType], Awaitable[Future[_UpdatedType]]]) -> KindN[_FutureLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @abstractmethod
    def bind_async(self, function: Callable[[_FirstType], Awaitable[KindN[_FutureLikeType, _UpdatedType, _SecondType, _ThirdType]]]) -> KindN[_FutureLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @abstractmethod
    def bind_awaitable(self, function: Callable[[_FirstType], Awaitable[_UpdatedType]]) -> KindN[_FutureLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @classmethod
    @abstractmethod
    def from_future(cls: Type[_FutureLikeType], inner_value: Future[_UpdatedType]) -> KindN[_FutureLikeType, _UpdatedType, _SecondType, _ThirdType]: ...

FutureLike1: Any
FutureLike2: Any
FutureLike3: Any

class AwaitableFutureN(metaclass=abc.ABCMeta):
    @abstractmethod
    def __await__(self) -> Generator[Any, Any, io.IOLikeN[_FirstType, _SecondType, _ThirdType]]: ...
    @abstractmethod
    async def awaitable(self) -> io.IOLikeN[_FirstType, _SecondType, _ThirdType]: ...

AsyncFuture1: Any
AsyncFuture2: Any
AsyncFuture3: Any

class FutureBasedN(FutureLikeN[_FirstType, _SecondType, _ThirdType], AwaitableFutureN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta): ...

FutureBased1: Any
FutureBased2: Any
FutureBased3: Any
