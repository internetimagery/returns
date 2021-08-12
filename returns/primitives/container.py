from __future__ import absolute_import
from abc import ABCMeta
from typing import Any, TypeVar

from returns.interfaces.equable import Equable
from returns.primitives.hkt import Kind1
from returns.primitives.types import Immutable

_EqualType = TypeVar(u'_EqualType', bound=Equable)


class BaseContainer(Immutable):
    __metaclass__ = ABCMeta
    u"""Utility class to provide all needed magic methods to the context."""

    __slots__ = (u'_inner_value',)
    _inner_value = None # type: Any

    def __init__(self, inner_value):
        u"""
        Wraps the given value in the Container.

        'value' is any arbitrary value of any type including functions.
        """
        object.__setattr__(self, u'_inner_value', inner_value)  # noqa: WPS609

    def __repr__(self):
        u"""Used to display details of object."""
        return u'<{0}: {1}>'.format(
            self.__class__.__qualname__.strip(u'_'),
            unicode(self._inner_value),
        )

    def __eq__(self, other):
        u"""Used to compare two 'Container' objects."""
        return container_equality(self, other)  # type: ignore

    def __hash__(self):
        u"""Used to use this value as a key."""
        return hash(self._inner_value)

    def __getstate__(self):
        u"""That's how this object will be pickled."""
        return self._inner_value

    def __setstate__(self, state):
        u"""Loading state from pickled data."""
        object.__setattr__(self, u'_inner_value', state)  # noqa: WPS609


def container_equality(
    self,
    other,
):
    u"""
    Function to compare similar containers.

    Compares both their types and their inner values.
    """
    if type(self) != type(other):  # noqa: WPS516
        return False
    return bool(
        self._inner_value == other._inner_value,  # type: ignore # noqa: WPS437
    )
