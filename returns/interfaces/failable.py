from __future__ import absolute_import
from abc import abstractmethod
from typing import Callable, ClassVar, NoReturn, Sequence, Type, TypeVar

from typing_extensions import final

from returns.interfaces import container as _container
from returns.interfaces import lashable, swappable
from returns.primitives.asserts import assert_equal
from returns.primitives.hkt import KindN
from returns.primitives.laws import (
    Law,
    Law2,
    Law3,
    Lawful,
    LawSpecDef,
    law_definition,
)

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_SingleFailableType = TypeVar(u'_SingleFailableType', bound=u'SingleFailableN')
_DiverseFailableType = TypeVar(u'_DiverseFailableType', bound=u'DiverseFailableN')

# Used in laws:
_NewFirstType = TypeVar(u'_NewFirstType')
_NewSecondType = TypeVar(u'_NewSecondType')


class _FailableLawSpec(LawSpecDef):
    u"""
    Failable laws.

    We need to be sure that ``.lash`` won't lash success types.
    """

    @law_definition
    def lash_short_circuit_law(
        raw_value,
        container,
        function,
    ):
        u"""Ensures that you cannot lash a success."""
        assert_equal(
            container.from_value(raw_value),
            container.from_value(raw_value).lash(function),
        )


_FailableLawSpec = final(_FailableLawSpec)

class FailableN(
    _container.ContainerN[_FirstType, _SecondType, _ThirdType],
    lashable.LashableN[_FirstType, _SecondType, _ThirdType],
    Lawful[u'FailableN[_FirstType, _SecondType, _ThirdType]'],
):
    u"""
    Base type for types that can fail.

    It is a raw type and should not be used directly.
    Use ``SingleFailableN`` and ``DiverseFailableN`` instead.
    """

    _laws = (
        Law3(_FailableLawSpec.lash_short_circuit_law),
    ) # type: ClassVar[Sequence[Law]]


#: Type alias for kinds with two type arguments.
Failable2 = FailableN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
Failable3 = FailableN[_FirstType, _SecondType, _ThirdType]


class _SingleFailableLawSpec(LawSpecDef):
    u"""
    Single Failable laws.

    We need to be sure that ``.map`` and ``.bind``
    works correctly for ``empty`` property.
    """

    @law_definition
    def map_short_circuit_law(
        container,
        function,
    ):
        u"""Ensures that you cannot map from the `empty` property."""
        assert_equal(
            container.empty,
            container.empty.map(function),
        )

    @law_definition
    def bind_short_circuit_law(
        container,
        function,
    ):
        u"""Ensures that you cannot bind from the `empty` property."""
        assert_equal(
            container.empty,
            container.empty.bind(function),
        )

    @law_definition
    def apply_short_circuit_law(
        container,
        function,
    ):
        u"""Ensures that you cannot apply from the `empty` property."""
        wrapped_function = container.from_value(function)
        assert_equal(
            container.empty,
            container.empty.apply(wrapped_function),
        )


_SingleFailableLawSpec = final(_SingleFailableLawSpec)

class SingleFailableN(
    FailableN[_FirstType, _SecondType, _ThirdType],
):
    u"""
    Base type for types that have just only one failed value.

    Like ``Maybe`` types where the only failed value is ``Nothing``.
    """

    _laws = (
        Law2(_SingleFailableLawSpec.map_short_circuit_law),
        Law2(_SingleFailableLawSpec.bind_short_circuit_law),
        Law2(_SingleFailableLawSpec.apply_short_circuit_law),
    ) # type: ClassVar[Sequence[Law]]

    @property
    @abstractmethod
    def empty(
        self,
    ):
        u"""This property represents the failed value."""


#: Type alias for kinds with two types arguments.
SingleFailable2 = SingleFailableN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
SingleFailable3 = SingleFailableN[_FirstType, _SecondType, _ThirdType]


class _DiverseFailableLawSpec(LawSpecDef):
    u"""
    Diverse Failable laws.

    We need to be sure that ``.map``, ``.bind``, ``.apply`` and ``.alt``
    works correctly for both success and failure types.
    """

    @law_definition
    def map_short_circuit_law(
        raw_value,
        container,
        function,
    ):
        u"""Ensures that you cannot map a failure."""
        assert_equal(
            container.from_failure(raw_value),
            container.from_failure(raw_value).map(function),
        )

    @law_definition
    def bind_short_circuit_law(
        raw_value,
        container,
        function,
    ):
        u"""
        Ensures that you cannot bind a failure.

        See: https://wiki.haskell.org/Typeclassopedia#MonadFail
        """
        assert_equal(
            container.from_failure(raw_value),
            container.from_failure(raw_value).bind(function),
        )

    @law_definition
    def apply_short_circuit_law(
        raw_value,
        container,
        function,
    ):
        u"""Ensures that you cannot apply a failure."""
        wrapped_function = container.from_value(function)
        assert_equal(
            container.from_failure(raw_value),
            container.from_failure(raw_value).apply(wrapped_function),
        )

    @law_definition
    def alt_short_circuit_law(
        raw_value,
        container,
        function,
    ):
        u"""Ensures that you cannot alt a success."""
        assert_equal(
            container.from_value(raw_value),
            container.from_value(raw_value).alt(function),
        )


_DiverseFailableLawSpec = final(_DiverseFailableLawSpec)

class DiverseFailableN(
    FailableN[_FirstType, _SecondType, _ThirdType],
    swappable.SwappableN[_FirstType, _SecondType, _ThirdType],
    Lawful[u'DiverseFailableN[_FirstType, _SecondType, _ThirdType]'],
):
    u"""
    Base type for types that have any failed value.

    Like ``Result`` types.
    """

    _laws = (
        Law3(_DiverseFailableLawSpec.map_short_circuit_law),
        Law3(_DiverseFailableLawSpec.bind_short_circuit_law),
        Law3(_DiverseFailableLawSpec.apply_short_circuit_law),
        Law3(_DiverseFailableLawSpec.alt_short_circuit_law),
    ) # type: ClassVar[Sequence[Law]]

    @classmethod
    @abstractmethod
    def from_failure(
        cls,
        inner_value,
    ):
        u"""Unit method to create new containers from any raw value."""


#: Type alias for kinds with two type arguments.
DiverseFailable2 = DiverseFailableN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
DiverseFailable3 = DiverseFailableN[_FirstType, _SecondType, _ThirdType]
