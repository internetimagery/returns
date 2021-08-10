from __future__ import absolute_import
from typing import Callable, ClassVar, Dict, Generic, Sequence, Type, TypeVar

from typing_extensions import final

from returns.primitives.types import Immutable

_Caps = TypeVar(u'_Caps')
_ReturnType = TypeVar(u'_ReturnType')
_TypeArgType1 = TypeVar(u'_TypeArgType1')
_TypeArgType2 = TypeVar(u'_TypeArgType2')
_TypeArgType3 = TypeVar(u'_TypeArgType3')

#: Special alias to define laws as functions even inside a class
law_definition = staticmethod


class Law(Immutable):
    u"""
    Base class for all laws. Does not have an attached signature.

    Should not be used directly.
    Use ``Law1``, ``Law2`` or ``Law3`` instead.
    """

    __slots__ = (u'definition', )

    #: Function used to define this law.
    definition: Callable

    def __init__(self, function):
        u"""Saves function to the inner state."""
        object.__setattr__(self, u'definition', function)  # noqa: WPS609

    @final
    @property
    def name(self):
        u"""Returns a name of the given law. Basically a name of the function."""
        return self.definition.__name__


class Law1(
    Law,
    Generic[_TypeArgType1, _ReturnType],
):
    u"""Law definition for functions with a single argument."""

    definition: Callable[[u'Law1', _TypeArgType1], _ReturnType]

    def __init__(
        self,
        function,
    ):
        u"""Saves function of one argument to the inner state."""
        super(Law1, self).__init__(function)


Law1 = final(Law1)

class Law2(
    Law,
    Generic[_TypeArgType1, _TypeArgType2, _ReturnType],
):
    u"""Law definition for functions with two arguments."""

    definition: Callable[[u'Law2', _TypeArgType1, _TypeArgType2], _ReturnType]

    def __init__(
        self,
        function,
    ):
        u"""Saves function of two arguments to the inner state."""
        super(Law2, self).__init__(function)


Law2 = final(Law2)

class Law3(
    Law,
    Generic[_TypeArgType1, _TypeArgType2, _TypeArgType3, _ReturnType],
):
    u"""Law definition for functions with three argument."""

    definition: Callable[
        [u'Law3', _TypeArgType1, _TypeArgType2, _TypeArgType3],
        _ReturnType,
    ]

    def __init__(
        self,
        function,
    ):
        u"""Saves function of three arguments to the inner state."""
        super(Law3, self).__init__(function)


Law3 = final(Law3)

class Lawful(Generic[_Caps]):
    u"""
    Base class for all lawful classes.

    Allows to smartly collect all defined laws from all parent classes.
    """

    #: Some classes and interfaces might have laws, some might not have any.
    _laws: ClassVar[Sequence[Law]]

    @final  # noqa: WPS210
    @classmethod
    def laws(cls):  # noqa: WPS210
        u"""
        Collects all laws from all parent classes.

        Algorithm:

        1. First, we collect all unique parents in ``__mro__``
        2. Then we get the laws definition from each of them
        3. Then we structure them in a ``type: its_laws`` way

        """
        seen = dict((
            u'{0}.{1}'.format(
                parent.__module__,  # noqa: WPS609
                parent.__qualname__,
            ), parent)
            for parent in cls.__mro__)

        laws = {}
        for klass in seen.values():
            current_laws = klass.__dict__.get(u'_laws', ())  # noqa: WPS609
            if not current_laws:
                continue
            laws[klass] = current_laws
        return laws


class LawSpecDef(object):
    u"""Base class for all collection of laws aka LawSpecs."""

    __slots__ = ()
