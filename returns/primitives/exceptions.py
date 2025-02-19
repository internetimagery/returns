from __future__ import absolute_import

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from returns.interfaces.unwrappable import Unwrappable  # noqa: WPS433


class UnwrapFailedError(Exception):
    u"""Raised when a container can not be unwrapped into a meaningful value."""

    __slots__ = (u'halted_container',)

    def __init__(self, container):
        u"""
        Saves halted container in the inner state.

        So, this container can later be unpacked from this exception
        and used as a regular value.
        """
        super(UnwrapFailedError, self).__init__()
        self.halted_container = container


class ImmutableStateError(AttributeError):
    u"""
    Raised when a container is forced to be mutated.

    It is a sublclass of ``AttributeError`` for two reasons:

    1. It seems kinda reasonable to expect ``AttributeError``
       on attribute modification
    2. It is used inside ``typing.py`` this way,
       we do have several typing features that requires that behaviour

    See: https://github.com/dry-python/returns/issues/394
    """
