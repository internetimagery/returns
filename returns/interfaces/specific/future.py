u"""
Represents the base interfaces for types that do fearless async operations.

This type means that ``Future`` cannot fail.
Don't use this type for async that can. Instead, use
:class:`returns.interfaces.specific.future_result.FutureResultBasedN` type.
"""

from __future__ import absolute_import
from __future__ import annotations

from abc import abstractmethod
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Generator,
    Generic,
    NoReturn,
    Type,
    TypeVar,
)

from trollius import coroutine

from returns.interfaces.specific import io
from returns.primitives.hkt import KindN

if TYPE_CHECKING:
    from returns.future import Future  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_FutureLikeType = TypeVar(u'_FutureLikeType', bound=u'FutureLikeN')
_AsyncFutureType = TypeVar(u'_AsyncFutureType', bound=u'AwaitableFutureN')
_FutureBasedType = TypeVar(u'_FutureBasedType', bound=u'FutureBasedN')


class FutureLikeN(io.IOLikeN[_FirstType, _SecondType, _ThirdType]):
    u"""
    Base type for ones that does look like ``Future``.

    But at the time this is not a real ``Future`` and cannot be awaited.
    """

    @abstractmethod
    def bind_future(
        self,
        function,
    ):
        u"""Allows to bind ``Future`` returning function over a container."""

    @abstractmethod
    def bind_async_future(
        self,
        function,
    ):
        u"""Allows to bind async ``Future`` returning function over container."""

    @abstractmethod
    def bind_async(
        self,
        function,
    ):
        u"""Binds async function returning the same type of container."""

    @abstractmethod
    def bind_awaitable(
        self,
        function,
    ):
        u"""Allows to bind async function over container."""

    @classmethod
    @abstractmethod
    def from_future(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Unit method to create new containers from successful ``Future``."""


#: Type alias for kinds with one type argument.
FutureLike1 = FutureLikeN[_FirstType, NoReturn, NoReturn]

#: Type alias for kinds with two type arguments.
FutureLike2 = FutureLikeN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
FutureLike3 = FutureLikeN[_FirstType, _SecondType, _ThirdType]


class AwaitableFutureN(Generic[_FirstType, _SecondType, _ThirdType]):
    u"""
    Type that provides the required API for ``Future`` to be async.

    Should not be used directly. Use ``FutureBasedN`` instead.
    """

    @abstractmethod
    def __await__(self):
        u"""Magic method to allow ``await`` expression."""

    @abstractmethod
    @coroutine
    def awaitable(
        self,
    ):
        u"""Underling logic under ``await`` expression."""


#: Type alias for kinds with one type argument.
AsyncFuture1 = AwaitableFutureN[_FirstType, NoReturn, NoReturn]

#: Type alias for kinds with two type arguments.
AsyncFuture2 = AwaitableFutureN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
AsyncFuture3 = AwaitableFutureN[_FirstType, _SecondType, _ThirdType]


class FutureBasedN(
    FutureLikeN[_FirstType, _SecondType, _ThirdType],
    AwaitableFutureN[_FirstType, _SecondType, _ThirdType],
):
    u"""
    Base type for real ``Future`` objects.

    They can be awaited.
    """


#: Type alias for kinds with one type argument.
FutureBased1 = FutureBasedN[_FirstType, NoReturn, NoReturn]

#: Type alias for kinds with two type arguments.
FutureBased2 = FutureBasedN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
FutureBased3 = FutureBasedN[_FirstType, _SecondType, _ThirdType]
