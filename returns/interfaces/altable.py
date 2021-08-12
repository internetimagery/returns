from __future__ import absolute_import
from abc import abstractmethod
from typing import Callable, ClassVar, Generic, NoReturn, Sequence, TypeVar

from typing_extensions import final

from returns.functions import compose, identity
from returns.primitives.asserts import assert_equal
from returns.primitives.hkt import KindN
from returns.primitives.laws import (
    Law,
    Law1,
    Law3,
    Lawful,
    LawSpecDef,
    law_definition,
)

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_AltableType = TypeVar(u'_AltableType', bound=u'AltableN')

# Used in laws:
_NewType1 = TypeVar(u'_NewType1')
_NewType2 = TypeVar(u'_NewType2')


class _LawSpec(LawSpecDef):
    u"""
    Mappable or functor laws.

    https://en.wikibooks.org/wiki/Haskell/The_Functor_class#The_functor_laws
    """

    @law_definition
    def identity_law(
        altable,
    ):
        u"""Mapping identity over a value must return the value unchanged."""
        assert_equal(altable.alt(identity), altable)

    @law_definition
    def associative_law(
        altable,
        first,
        second,
    ):
        u"""Mapping twice or mapping a composition is the same thing."""
        assert_equal(
            altable.alt(first).alt(second),
            altable.alt(compose(first, second)),
        )


_LawSpec = final(_LawSpec)

class AltableN(
    Generic[_FirstType, _SecondType, _ThirdType],
    Lawful[u'AltableN[_FirstType, _SecondType, _ThirdType]'],
):
    u"""Modifies the second type argument with a pure function."""

    _laws = (
        Law1(_LawSpec.identity_law),
        Law3(_LawSpec.associative_law),
    ) # type: ClassVar[Sequence[Law]]

    @abstractmethod
    def alt(
        self,
        function,
    ):
        u"""Allows to run a pure function over a container."""


#: Type alias for kinds with two type arguments.
Altable2 = AltableN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
Altable3 = AltableN[_FirstType, _SecondType, _ThirdType]
