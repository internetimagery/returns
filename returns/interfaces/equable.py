from __future__ import absolute_import
from abc import abstractmethod
from typing import ClassVar, Sequence, TypeVar

from typing_extensions import final

from returns.primitives.laws import (
    Law,
    Law1,
    Law2,
    Law3,
    Lawful,
    LawSpecDef,
    law_definition,
)

_EqualType = TypeVar(u'_EqualType', bound=u'Equable')


class _LawSpec(LawSpecDef):
    u"""
    Equality laws.

    Description: https://bit.ly/34D40iT
    """

    @law_definition
    def reflexive_law(
        first,
    ):
        u"""Value should be equal to itself."""
        assert first.equals(first)

    @law_definition
    def symmetry_law(
        first,
        second,
    ):
        u"""If ``A == B`` then ``B == A``."""
        assert first.equals(second) == second.equals(first)

    @law_definition
    def transitivity_law(
        first,
        second,
        third,
    ):
        u"""If ``A == B`` and ``B == C`` then ``A == C``."""
        # We use this notation, because `first` might be equal to `third`,
        # but not to `second`. Example: Some(1), Some(2), Some(1)
        if first.equals(second) and second.equals(third):
            assert first.equals(third)


_LawSpec = final(_LawSpec)

class Equable(Lawful[u'Equable']):
    u"""
    Interface for types that can be compared with real values.

    Not all types can, because some don't have the value at a time:
    - ``Future`` has to be awaited to get the value
    - ``Reader`` has to be called to get the value

    """

    _laws: ClassVar[Sequence[Law]] = (
        Law1(_LawSpec.reflexive_law),
        Law2(_LawSpec.symmetry_law),
        Law3(_LawSpec.transitivity_law),
    )

    @abstractmethod
    def equals(self, other):
        u"""Type-safe equality check for values of the same type."""
