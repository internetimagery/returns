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

_MappableType = TypeVar(u'_MappableType', bound=u'MappableN')

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
        mappable,
    ):
        u"""Mapping identity over a value must return the value unchanged."""
        assert_equal(mappable.map(identity), mappable)

    @law_definition
    def associative_law(
        mappable,
        first,
        second,
    ):
        u"""Mapping twice or mapping a composition is the same thing."""
        assert_equal(
            mappable.map(first).map(second),
            mappable.map(compose(first, second)),
        )


_LawSpec = final(_LawSpec)

class MappableN(
    Generic[_FirstType, _SecondType, _ThirdType],
    Lawful[u'MappableN[_FirstType, _SecondType, _ThirdType]'],
):
    u"""
    Allows to chain wrapped values in containers with regular functions.

    Behaves like a functor.

    See also:
        - https://en.wikipedia.org/wiki/Functor

    """

    _laws: ClassVar[Sequence[Law]] = (
        Law1(_LawSpec.identity_law),
        Law3(_LawSpec.associative_law),
    )

    @abstractmethod  # noqa: WPS125
    def map(
        self,
        function,
    ):
        u"""Allows to run a pure function over a container."""


#: Type alias for kinds with one type argument.
Mappable1 = MappableN[_FirstType, NoReturn, NoReturn]

#: Type alias for kinds with two type arguments.
Mappable2 = MappableN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
Mappable3 = MappableN[_FirstType, _SecondType, _ThirdType]
