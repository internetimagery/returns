from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.interfaces.bimappable import BiMappableN
from returns.primitives.hkt import Kinded, KindN, kinded

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')

_UpdatedType1 = TypeVar(u'_UpdatedType1')
_UpdatedType2 = TypeVar(u'_UpdatedType2')

_BiMappableKind = TypeVar(u'_BiMappableKind', bound=BiMappableN)


def bimap(
    on_first,
    on_second,
):
    u"""
    Maps container on both: first and second arguments.

    Can be used to synchronize state on both success and failure.

    This is how it should be used:

    .. code:: python

        >>> from returns.io import IOSuccess, IOFailure
        >>> from returns.pointfree import bimap

        >>> def first(argument: int) -> float:
        ...     return argument / 2

        >>> def second(argument: str) -> bool:
        ...     return bool(argument)

        >>> assert bimap(first, second)(IOSuccess(1)) == IOSuccess(0.5)
        >>> assert bimap(first, second)(IOFailure('')) == IOFailure(False)

    Note, that this function works
    for all containers with ``.map`` and ``.alt`` methods.
    See :class:`returns.primitives.interfaces.bimappable.BiMappableN`
    for more info.

    """
    @kinded
    def factory(
        container,
    ):
        return container.map(on_first).alt(on_second)
    return factory
