from __future__ import absolute_import
from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Callable, ClassVar, Sequence, Type, TypeVar

from returns.interfaces.specific import ioresult, reader, reader_result
from returns.primitives.hkt import KindN
from returns.primitives.laws import (
    Law,
    Law2,
    Lawful,
    LawSpecDef,
    law_definition,
)

if TYPE_CHECKING:
    from returns.context import ReaderIOResult  # noqa: WPS433
    from returns.io import IOResult  # noqa: F401, WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_ValueType = TypeVar(u'_ValueType')
_ErrorType = TypeVar(u'_ErrorType')
_EnvType = TypeVar(u'_EnvType')

_ReaderIOResultLikeType = TypeVar(
    u'_ReaderIOResultLikeType',
    bound=u'ReaderIOResultLikeN',
)


class ReaderIOResultLikeN(
    reader_result.ReaderResultLikeN[_FirstType, _SecondType, _ThirdType],
    ioresult.IOResultLikeN[_FirstType, _SecondType, _ThirdType],
):
    u"""
    Base interface for all types that do look like ``ReaderIOResult`` instance.

    Cannot be called.
    """

    @abstractmethod
    def bind_context_ioresult(
        self,
        function,
    ):
        u"""Binds a ``ReaderIOResult`` returning function over a container."""

    @classmethod
    @abstractmethod
    def from_ioresult_context(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Unit method to create new containers from ``ReaderIOResult``."""


#: Type alias for kinds with three type arguments.
ReaderIOResultLike3 = ReaderIOResultLikeN[_FirstType, _SecondType, _ThirdType]


class _LawSpec(LawSpecDef):
    u"""
    Concrete laws for ``ReaderIOResultBasedN``.

    See: https://github.com/haskell/mtl/pull/61/files
    """

    @law_definition
    def asking_law(
        container,
        env,
    ):
        u"""Asking for an env, always returns the env."""
        assert container.ask().__call__(    # noqa: WPS609
            env,
        ) == container.from_value(env).__call__(env)  # noqa: WPS609


class ReaderIOResultBasedN(
    ReaderIOResultLikeN[_FirstType, _SecondType, _ThirdType],
    reader.CallableReader3[
        _FirstType,
        _SecondType,
        _ThirdType,
        # Calls:
        u'IOResult[_FirstType, _SecondType]',
        _ThirdType,
    ],
    Lawful[u'ReaderIOResultBasedN[_FirstType, _SecondType, _ThirdType]'],
):
    u"""
    This interface is very specific to our ``ReaderIOResult`` type.

    The only thing that differs from ``ReaderIOResultLikeN`` is that we know
    the specific types for its ``__call__`` method.

    In this case the return type of ``__call__`` is ``IOResult``.
    """

    _laws: ClassVar[Sequence[Law]] = (
        Law2(_LawSpec.asking_law),
    )


#: Type alias for kinds with three type arguments.
ReaderIOResultBased3 = ReaderIOResultBasedN[_FirstType, _SecondType, _ThirdType]
