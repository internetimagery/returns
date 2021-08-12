u"""
An interface for types that do ``IO`` and can fail.

It is a base interface for both sync and async ``IO`` stacks.
"""

from __future__ import absolute_import

from abc import abstractmethod
from typing import TYPE_CHECKING, Callable, NoReturn, Type, TypeVar

from returns.interfaces.specific import io, result
from returns.primitives.hkt import KindN

if TYPE_CHECKING:
    from returns.io import IO, IOResult  # noqa: WPS433
    from returns.result import Result  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_ValueType = TypeVar(u'_ValueType')
_ErrorType = TypeVar(u'_ErrorType')

_IOResultLikeType = TypeVar(u'_IOResultLikeType', bound=u'IOResultLikeN')


class IOResultLikeN(
    io.IOLikeN[_FirstType, _SecondType, _ThirdType],
    result.ResultLikeN[_FirstType, _SecondType, _ThirdType],
):
    u"""
    Base type for types that look like ``IOResult`` but cannot be unwrapped.

    Like ``FutureResult`` or ``RequiresContextIOResult``.
    """

    @abstractmethod
    def bind_ioresult(
        self,
        function,
    ):
        u"""Runs ``IOResult`` returning function over a container."""

    @abstractmethod
    def compose_result(
        self,
        function,
    ):
        u"""Allows to compose the underlying ``Result`` with a function."""

    @classmethod
    @abstractmethod
    def from_ioresult(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Unit method to create new containers from ``IOResult`` type."""

    @classmethod
    @abstractmethod
    def from_failed_io(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Unit method to create new containers from failed ``IO``."""


#: Type alias for kinds with two type arguments.
IOResultLike2 = IOResultLikeN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
IOResultLike3 = IOResultLikeN[_FirstType, _SecondType, _ThirdType]


class IOResultBasedN(
    IOResultLikeN[_FirstType, _SecondType, _ThirdType],
    io.IOBasedN[_FirstType, _SecondType, _ThirdType],
    result.UnwrappableResult[
        _FirstType,
        _SecondType,
        _ThirdType,
        # Unwraps:
        u'IO[_FirstType]',
        u'IO[_SecondType]',
    ],
):
    u"""
    Base type for real ``IOResult`` types.

    Can be unwrapped.
    """


#: Type alias for kinds with two type arguments.
IOResultBased2 = IOResultBasedN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
IOResultBased3 = IOResultBasedN[_FirstType, _SecondType, _ThirdType]
