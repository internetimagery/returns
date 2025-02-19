u"""
Represents the base interfaces for types that do fear-some async operations.

This type means that ``FutureResult`` can (and will!) fail with exceptions.

Use this type to mark that this specific async opetaion can fail.
"""

from __future__ import absolute_import

from abc import abstractmethod
from typing import TYPE_CHECKING, Callable, NoReturn, Type, TypeVar

from returns.interfaces.specific import future, ioresult
from returns.primitives.hkt import KindN

if TYPE_CHECKING:
    from typing import Awaitable
    from returns.future import Future, FutureResult  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_ValueType = TypeVar(u'_ValueType')
_ErrorType = TypeVar(u'_ErrorType')

_FutureResultLikeType = TypeVar(
    u'_FutureResultLikeType', bound=u'FutureResultLikeN',
)


class FutureResultLikeN(
    future.FutureLikeN[_FirstType, _SecondType, _ThirdType],
    ioresult.IOResultLikeN[_FirstType, _SecondType, _ThirdType],
):
    u"""
    Base type for ones that does look like ``FutureResult``.

    But at the time this is not a real ``Future`` and cannot be awaited.
    It is also cannot be unwrapped, because it is not a real ``IOResult``.
    """

    @abstractmethod
    def bind_future_result(
        self,
        function,
    ):
        u"""Allows to bind ``FutureResult`` functions over a container."""

    @abstractmethod
    def bind_async_future_result(
        self,
        function,
    ):
        u"""Allows to bind async ``FutureResult`` functions over container."""

    @classmethod
    @abstractmethod
    def from_failed_future(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Creates new container from a failed ``Future``."""

    @classmethod
    def from_future_result(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Creates container from ``FutureResult`` instance."""


#: Type alias for kinds with two type arguments.
FutureResultLike2 = FutureResultLikeN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
FutureResultLike3 = FutureResultLikeN[_FirstType, _SecondType, _ThirdType]


class FutureResultBasedN(
    future.FutureBasedN[_FirstType, _SecondType, _ThirdType],
    FutureResultLikeN[_FirstType, _SecondType, _ThirdType],
):
    u"""
    Base type for real ``FutureResult`` objects.

    They can be awaited.
    Still cannot be unwrapped.
    """


#: Type alias for kinds with two type arguments.
FutureResultBased2 = FutureResultBasedN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
FutureResultBased3 = FutureResultBasedN[_FirstType, _SecondType, _ThirdType]
