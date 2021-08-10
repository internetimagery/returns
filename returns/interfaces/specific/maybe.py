from __future__ import absolute_import
from abc import abstractmethod
from typing import (
    Callable,
    ClassVar,
    NoReturn,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
)

from typing_extensions import final

from returns.interfaces import equable, failable, unwrappable
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

_MaybeLikeType = TypeVar(u'_MaybeLikeType', bound=u'MaybeLikeN')

# New values:
_ValueType = TypeVar(u'_ValueType')

# Only used in laws:
_NewType1 = TypeVar(u'_NewType1')


class _LawSpec(LawSpecDef):
    u"""
    Maybe laws.

    We need to be sure that
    ``.map``, ``.bind``, ``.bind_optional``, and ``.lash``
    works correctly for both successful and failed types.
    """

    @law_definition
    def map_short_circuit_law(
        container,
        function,
    ):
        u"""Ensures that you cannot map from failures."""
        assert_equal(
            container.from_optional(None).map(function),
            container.from_optional(None),
        )

    @law_definition
    def bind_short_circuit_law(
        container,
        function,
    ):
        u"""Ensures that you cannot bind from failures."""
        assert_equal(
            container.from_optional(None).bind(function),
            container.from_optional(None),
        )

    @law_definition
    def bind_optional_short_circuit_law(
        container,
        function,
    ):
        u"""Ensures that you cannot bind from failures."""
        assert_equal(
            container.from_optional(None).bind_optional(function),
            container.from_optional(None),
        )

    @law_definition
    def lash_short_circuit_law(
        raw_value,
        container,
        function,
    ):
        u"""Ensures that you cannot lash a success."""
        assert_equal(
            container.from_value(raw_value).lash(function),
            container.from_value(raw_value),
        )

    @law_definition
    def unit_structure_law(
        container,
        function,
    ):
        u"""Ensures ``None`` is treated specially."""
        assert_equal(
            container.bind_optional(function),
            container.from_optional(None),
        )


_LawSpec = final(_LawSpec)

class MaybeLikeN(
    failable.SingleFailableN[_FirstType, _SecondType, _ThirdType],
    Lawful[u'MaybeLikeN[_FirstType, _SecondType, _ThirdType]'],
):
    u"""
    Type for values that do look like a ``Maybe``.

    For example, ``RequiresContextMaybe`` should be created from this interface.
    Cannot be unwrapped or compared.
    """

    _laws: ClassVar[Sequence[Law]] = (
        Law2(_LawSpec.map_short_circuit_law),
        Law2(_LawSpec.bind_short_circuit_law),
        Law2(_LawSpec.bind_optional_short_circuit_law),
        Law3(_LawSpec.lash_short_circuit_law),
        Law2(_LawSpec.unit_structure_law),
    )

    @abstractmethod
    def bind_optional(
        self,
        function,
    ):
        u"""Binds a function that returns ``Optional`` values."""

    @classmethod
    @abstractmethod
    def from_optional(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Unit method to create containers from ``Optional`` value."""


#: Type alias for kinds with two type arguments.
MaybeLike2 = MaybeLikeN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
MaybeLike3 = MaybeLikeN[_FirstType, _SecondType, _ThirdType]


class MaybeBasedN(
    MaybeLikeN[_FirstType, _SecondType, _ThirdType],
    unwrappable.Unwrappable[_FirstType, None],
    equable.Equable,
):
    u"""
    Concrete interface for ``Maybe`` type.

    Can be unwrapped and compared.
    """

    @abstractmethod
    def or_else_call(
        self,
        function,
    ):
        u"""Calls a function in case there nothing to unwrap."""


#: Type alias for kinds with two type arguments.
MaybeBased2 = MaybeBasedN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
MaybeBased3 = MaybeBasedN[_FirstType, _SecondType, _ThirdType]
