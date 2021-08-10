from __future__ import absolute_import
from abc import abstractmethod
from typing import Callable, NoReturn, Tuple, Type, TypeVar

from typing_extensions import final

from returns.interfaces import bindable, equable, lashable, swappable
from returns.primitives.container import BaseContainer, container_equality
from returns.primitives.hkt import Kind2, KindN, SupportsKind2, dekind

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')

_NewFirstType = TypeVar(u'_NewFirstType')
_NewSecondType = TypeVar(u'_NewSecondType')

_PairLikeKind = TypeVar(u'_PairLikeKind', bound=u'PairLikeN')


class PairLikeN(
    bindable.BindableN[_FirstType, _SecondType, _ThirdType],
    swappable.SwappableN[_FirstType, _SecondType, _ThirdType],
    lashable.LashableN[_FirstType, _SecondType, _ThirdType],
    equable.Equable,
):
    u"""Special interface for types that look like a ``Pair``."""

    @abstractmethod
    def pair(
        self,
        function,
    ):
        u"""Allows to work with both arguments at the same time."""

    @classmethod
    @abstractmethod
    def from_paired(
        cls,
        first,
        second,
    ):
        u"""Allows to create a PairLikeN from just two values."""

    @classmethod
    @abstractmethod
    def from_unpaired(
        cls,
        inner_value,
    ):
        u"""Allows to create a PairLikeN from just a single object."""


PairLike2 = PairLikeN[_FirstType, _SecondType, NoReturn]
PairLike3 = PairLikeN[_FirstType, _SecondType, _ThirdType]


class Pair(
    BaseContainer,
    SupportsKind2[u'Pair', _FirstType, _SecondType],
    PairLike2[_FirstType, _SecondType],
):
    u"""
    A type that represents a pair of something.

    Like to coordinates ``(x, y)`` or two best friends.
    Or a question and an answer.

    """

    def __init__(
        self,
        inner_value,
    ):
        u"""Saves passed tuple as ``._inner_value`` inside this instance."""
        super(Pair, self).__init__(inner_value)

    # `Equable` part:

    equals = container_equality  # we already have this defined for all types

    # `Mappable` part via `BiMappable`:

    def map(
        self,
        function,
    ):
        u"""
        Changes the first type with a pure function.

        >>> assert Pair((1, 2)).map(str) == Pair(('1', 2))

        """
        return Pair((function(self._inner_value[0]), self._inner_value[1]))

    # `BindableN` part:

    def bind(
        self,
        function,
    ):
        u"""
        Changes the first type with a function returning another ``Pair``.

        >>> def bindable(first: int) -> Pair[str, str]:
        ...     return Pair((str(first), ''))

        >>> assert Pair((1, 'b')).bind(bindable) == Pair(('1', ''))

        """
        return dekind(function(self._inner_value[0]))

    # `AltableN` part via `BiMappableN`:

    def alt(
        self,
        function,
    ):
        u"""
        Changes the second type with a pure function.

        >>> assert Pair((1, 2)).alt(str) == Pair((1, '2'))

        """
        return Pair((self._inner_value[0], function(self._inner_value[1])))

    # `LashableN` part:

    def lash(
        self,
        function,
    ):
        u"""
        Changes the second type with a function returning ``Pair``.

        >>> def lashable(second: int) -> Pair[str, str]:
        ...     return Pair(('', str(second)))

        >>> assert Pair(('a', 2)).lash(lashable) == Pair(('', '2'))

        """
        return dekind(function(self._inner_value[1]))

    # `SwappableN` part:

    def swap(self):
        u"""
        Swaps ``Pair`` elements.

        >>> assert Pair((1, 2)).swap() == Pair((2, 1))

        """
        return Pair((self._inner_value[1], self._inner_value[0]))

    # `PairLikeN` part:

    def pair(
        self,
        function,
    ):
        u"""
        Creates a new ``Pair`` from an existing one via a passed function.

        >>> def min_max(first: int, second: int) -> Pair[int, int]:
        ...     return Pair((min(first, second), max(first, second)))

        >>> assert Pair((2, 1)).pair(min_max) == Pair((1, 2))
        >>> assert Pair((1, 2)).pair(min_max) == Pair((1, 2))

        """
        return dekind(function(self._inner_value[0], self._inner_value[1]))

    @classmethod
    def from_paired(
        cls,
        first,
        second,
    ):
        u"""
        Creates a new pair from two values.

        >>> assert Pair.from_paired(1, 2) == Pair((1, 2))

        """
        return Pair((first, second))

    @classmethod
    def from_unpaired(
        cls,
        inner_value,
    ):
        u"""
        Creates a new pair from a single value.

        >>> assert Pair.from_unpaired(1) == Pair((1, 1))

        """
        return Pair((inner_value, inner_value))

Pair = final(Pair)
