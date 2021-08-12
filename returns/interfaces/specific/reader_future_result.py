from __future__ import absolute_import

from abc import abstractmethod
from typing import (
    TYPE_CHECKING,
    Callable,
    ClassVar,
    Sequence,
    Type,
    TypeVar,
)

from returns.interfaces.specific import future_result, reader, reader_ioresult
from returns.primitives.asserts import assert_equal
from returns.primitives.hkt import KindN
from returns.primitives.laws import (
    Law,
    Law2,
    Lawful,
    LawSpecDef,
    law_definition,
)

if TYPE_CHECKING:
    from returns.context import ReaderFutureResult  # noqa: WPS433
    from returns.future import FutureResult  # noqa: F401, WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_ValueType = TypeVar(u'_ValueType')
_ErrorType = TypeVar(u'_ErrorType')
_EnvType = TypeVar(u'_EnvType')

_ReaderFutureResultLikeType = TypeVar(
    u'_ReaderFutureResultLikeType',
    bound=u'ReaderFutureResultLikeN',
)


class ReaderFutureResultLikeN(
    reader_ioresult.ReaderIOResultLikeN[_FirstType, _SecondType, _ThirdType],
    future_result.FutureResultLikeN[_FirstType, _SecondType, _ThirdType],
):
    u"""
    Interface for all types that do look like ``ReaderFutureResult`` instance.

    Cannot be called.
    """

    @abstractmethod
    def bind_context_future_result(
        self,
        function,
    ):
        u"""Bind a ``ReaderFutureResult`` returning function over a container."""

    @abstractmethod
    def bind_async_context_future_result(
        self,
        function,
    ):
        u"""Bind async ``ReaderFutureResult`` function."""

    @classmethod
    @abstractmethod
    def from_future_result_context(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Unit method to create new containers from ``ReaderFutureResult``."""


#: Type alias for kinds with three type arguments.
ReaderFutureResultLike3 = ReaderFutureResultLikeN[
    _FirstType, _SecondType, _ThirdType,
]


class _LawSpec(LawSpecDef):
    u"""
    Concrete laws for ``ReaderFutureResultBasedN``.

    See: https://github.com/haskell/mtl/pull/61/files
    """

    @law_definition
    def asking_law(
        container,
        env,
    ):
        u"""Asking for an env, always returns the env."""
        assert_equal(
            container.ask().__call__(env),  # noqa: WPS609
            container.from_value(env).__call__(env),  # noqa: WPS609
        )


class ReaderFutureResultBasedN(
    ReaderFutureResultLikeN[_FirstType, _SecondType, _ThirdType],
    reader.CallableReader3[
        _FirstType,
        _SecondType,
        _ThirdType,
        # Calls:
        u'FutureResult[_FirstType, _SecondType]',
        _ThirdType,
    ],
    Lawful[u'ReaderFutureResultBasedN[_FirstType, _SecondType, _ThirdType]'],
):
    u"""
    This interface is very specific to our ``ReaderFutureResult`` type.

    The only thing that differs from ``ReaderFutureResultLikeN``
    is that we know the specific types for its ``__call__`` method.

    In this case the return type of ``__call__`` is ``FutureResult``.
    """

    _laws = (
        Law2(_LawSpec.asking_law),
    ) # type: ClassVar[Sequence[Law]]


#: Type alias for kinds with three type arguments.
ReaderFutureResultBased3 = ReaderFutureResultBasedN[
    _FirstType, _SecondType, _ThirdType,
]
