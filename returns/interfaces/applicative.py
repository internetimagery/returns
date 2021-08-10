from __future__ import absolute_import
from abc import abstractmethod
from typing import Callable, ClassVar, NoReturn, Sequence, Type, TypeVar

from typing_extensions import final

from returns.functions import compose, identity
from returns.interfaces import mappable
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

_ApplicativeType = TypeVar(u'_ApplicativeType', bound=u'ApplicativeN')

# Only used in laws:
_NewType1 = TypeVar(u'_NewType1')
_NewType2 = TypeVar(u'_NewType2')


class _LawSpec(LawSpecDef):
    u"""
    Applicative mappable laws.

    Definition: https://bit.ly/3hC8F8E
    Discussion: https://bit.ly/3jffz3L
    """

    @law_definition
    def identity_law(
        container,
    ):
        u"""
        Identity law.

        If we apply wrapped ``identity`` function to a container,
        nothing happens.
        """
        assert_equal(
            container,
            container.apply(container.from_value(identity)),
        )

    @law_definition
    def interchange_law(
        raw_value,
        container,
        function,
    ):
        u"""
        Interchange law.

        Basically we check that we can start our composition
        with both ``raw_value`` and ``function``.

        Great explanation: https://stackoverflow.com/q/27285918/4842742
        """
        assert_equal(
            container.from_value(raw_value).apply(
                container.from_value(function),
            ),
            container.from_value(function).apply(
                container.from_value(lambda inner: inner(raw_value)),
            ),
        )

    @law_definition
    def homomorphism_law(
        raw_value,
        container,
        function,
    ):
        u"""
        Homomorphism law.

        The homomorphism law says that
        applying a wrapped function to a wrapped value is the same
        as applying the function to the value in the normal way
        and then using ``.from_value`` on the result.
        """
        assert_equal(
            container.from_value(function(raw_value)),
            container.from_value(raw_value).apply(
                container.from_value(function),
            ),
        )

    @law_definition
    def composition_law(
        container,
        first,
        second,
    ):
        u"""
        Composition law.

        Applying two functions twice is the same
        as applying their composition once.
        """
        assert_equal(
            container.apply(container.from_value(compose(first, second))),
            container.apply(
                container.from_value(first),
            ).apply(
                container.from_value(second),
            ),
        )


_LawSpec = final(_LawSpec)

class ApplicativeN(
    mappable.MappableN[_FirstType, _SecondType, _ThirdType],
    Lawful[u'ApplicativeN[_FirstType, _SecondType, _ThirdType]'],
):
    u"""
    Allows to create unit containers from raw values and to apply wrapped funcs.

    See also:
        - https://en.wikipedia.org/wiki/Applicative_functor
        - http://learnyouahaskell.com/functors-applicative-functors-and-monoids

    """

    _laws: ClassVar[Sequence[Law]] = (
        Law1(_LawSpec.identity_law),
        Law3(_LawSpec.interchange_law),
        Law3(_LawSpec.homomorphism_law),
        Law3(_LawSpec.composition_law),
    )

    @abstractmethod
    def apply(
        self,
        container,
    ):
        u"""Allows to apply a wrapped function over a container."""

    @classmethod
    @abstractmethod
    def from_value(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Unit method to create new containers from any raw value."""


#: Type alias for kinds with one type argument.
Applicative1 = ApplicativeN[_FirstType, NoReturn, NoReturn]

#: Type alias for kinds with two type arguments.
Applicative2 = ApplicativeN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
Applicative3 = ApplicativeN[_FirstType, _SecondType, _ThirdType]
