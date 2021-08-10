from __future__ import absolute_import
from abc import abstractmethod
from typing import ClassVar, NoReturn, Sequence, TypeVar

from typing_extensions import final

from returns.interfaces import bimappable
from returns.primitives.asserts import assert_equal
from returns.primitives.hkt import KindN
from returns.primitives.laws import (
    Law,
    Law1,
    Lawful,
    LawSpecDef,
    law_definition,
)

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')

_SwappableType = TypeVar(u'_SwappableType', bound=u'SwappableN')


class _LawSpec(LawSpecDef):
    u"""Laws for :class:`~SwappableN` type."""

    @law_definition
    def double_swap_law(
        container,
    ):
        u"""
        Swaaping container twice.

        It ensure that we get the initial value back.
        In other words, swapping twice does nothing.
        """
        assert_equal(
            container,
            container.swap().swap(),
        )


_LawSpec = final(_LawSpec)

class SwappableN(
    bimappable.BiMappableN[_FirstType, _SecondType, _ThirdType],
    Lawful[u'SwappableN[_FirstType, _SecondType, _ThirdType]'],
):
    u"""Interface that allows swapping first and second type values."""

    _laws: ClassVar[Sequence[Law]] = (
        Law1(_LawSpec.double_swap_law),
    )

    @abstractmethod
    def swap(
        self,
    ):
        u"""Swaps first and second types in ``SwappableN``."""


#: Type alias for kinds with two type arguments.
Swappable2 = SwappableN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
Swappable3 = SwappableN[_FirstType, _SecondType, _ThirdType]
