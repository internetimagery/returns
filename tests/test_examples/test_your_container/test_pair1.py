from __future__ import absolute_import
from typing import Callable, Tuple, TypeVar

from typing_extensions import final

from returns.interfaces import bindable, equable, lashable, swappable
from returns.primitives.container import BaseContainer, container_equality
from returns.primitives.hkt import Kind2, SupportsKind2, dekind

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')

_NewFirstType = TypeVar(u'_NewFirstType')
_NewSecondType = TypeVar(u'_NewSecondType')


class Pair(
    BaseContainer,
    SupportsKind2[u'Pair', _FirstType, _SecondType],
    bindable.Bindable2[_FirstType, _SecondType],
    swappable.Swappable2[_FirstType, _SecondType],
    lashable.Lashable2[_FirstType, _SecondType],
    equable.Equable,
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
        return Pair((function(self._inner_value[0]), self._inner_value[1]))

    # `BindableN` part:

    def bind(
        self,
        function,
    ):
        return dekind(function(self._inner_value[0]))

    # `AltableN` part via `BiMappableN`:

    def alt(
        self,
        function,
    ):
        return Pair((self._inner_value[0], function(self._inner_value[1])))

    # `LashableN` part:

    def lash(
        self,
        function,
    ):
        return dekind(function(self._inner_value[1]))

    # `SwappableN` part:

    def swap(self):
        return Pair((self._inner_value[1], self._inner_value[0]))

Pair = final(Pair)
