u"""
An interface that represents a pure computation result.

For impure result see
:class:`returns.interfaces.specific.ioresult.IOResultLikeN` type.
"""

from __future__ import absolute_import
from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Callable, NoReturn, Type, TypeVar

from returns.interfaces import equable, failable, unwrappable
from returns.primitives.hkt import KindN

if TYPE_CHECKING:
    from returns.result import Result  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_ResultLikeType = TypeVar(u'_ResultLikeType', bound=u'ResultLikeN')

# New values:
_ValueType = TypeVar(u'_ValueType')
_ErrorType = TypeVar(u'_ErrorType')

# Unwrappable:
_FirstUnwrappableType = TypeVar(u'_FirstUnwrappableType')
_SecondUnwrappableType = TypeVar(u'_SecondUnwrappableType')


class ResultLikeN(
    failable.DiverseFailableN[_FirstType, _SecondType, _ThirdType],
):
    u"""
    Base types for types that looks like ``Result`` but cannot be unwrapped.

    Like ``RequiresContextResult`` or ``FutureResult``.
    """

    @abstractmethod
    def bind_result(
        self,
        function,
    ):
        u"""Runs ``Result`` returning function over a container."""

    @classmethod
    @abstractmethod
    def from_result(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Unit method to create new containers from any raw value."""


#: Type alias for kinds with two type arguments.
ResultLike2 = ResultLikeN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
ResultLike3 = ResultLikeN[_FirstType, _SecondType, _ThirdType]


class UnwrappableResult(
    ResultLikeN[_FirstType, _SecondType, _ThirdType],
    unwrappable.Unwrappable[_FirstUnwrappableType, _SecondUnwrappableType],
    equable.Equable,
):
    u"""
    Intermediate type with 5 type arguments that represents unwrappable result.

    It is a raw type and should not be used directly.
    Use ``ResultBasedN`` and ``IOResultBasedN`` instead.
    """


class ResultBasedN(
    UnwrappableResult[
        _FirstType,
        _SecondType,
        _ThirdType,
        # Unwraps:
        _FirstType,
        _SecondType,
    ],
):
    u"""
    Base type for real ``Result`` types.

    Can be unwrapped.
    """


#: Type alias for kinds with two type arguments.
ResultBased2 = ResultBasedN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
ResultBased3 = ResultBasedN[_FirstType, _SecondType, _ThirdType]
