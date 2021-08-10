from __future__ import absolute_import
from abc import abstractmethod
from typing import Generic, TypeVar

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')

_UnwrappableType = TypeVar(u'_UnwrappableType', bound=u'Unwrappable')


class Unwrappable(Generic[_FirstType, _SecondType]):
    u"""
    Represents containers that can unwrap and return its wrapped value.

    There are no aliases or ``UnwrappableN`` for ``Unwrappable`` interface.
    Because it always uses two and just two types.

    Not all types can be ``Unwrappable`` because we do require
    to raise ``UnwrapFailedError`` if unwrap is not possible.
    """

    @abstractmethod
    def unwrap(self):
        u"""
        Custom magic method to unwrap inner value from container.

        Should be redefined for ones that actually have values.
        And for ones that raise an exception for no values.

        .. note::
            As a part of the contract, failed ``unwrap`` calls
            must raise :class:`returns.primitives.exceptions.UnwrapFailedError`
            exception.

        This method is the opposite of :meth:`~Unwrapable.failure`.
        """

    @abstractmethod
    def failure(self):
        u"""
        Custom magic method to unwrap inner value from the failed container.

        .. note::
            As a part of the contract, failed ``failure`` calls
            must raise :class:`returns.primitives.exceptions.UnwrapFailedError`
            exception.

        This method is the opposite of :meth:`~Unwrapable.unwrap`.
        """
