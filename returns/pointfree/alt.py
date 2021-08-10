from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.interfaces.altable import AltableN
from returns.primitives.hkt import Kinded, KindN, kinded

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_AltableKind = TypeVar(u'_AltableKind', bound=AltableN)


def alt(
    function,
):
    u"""
    Lifts function to be wrapped in a container for better composition.

    In other words, it modifies the function's
    signature from:
    ``a -> b``
    to:
    ``Container[a] -> Container[b]``

    This is how it should be used:

    .. code:: python

        >>> from returns.io import IOFailure, IOSuccess
        >>> from returns.pointfree import alt

        >>> def example(argument: int) -> float:
        ...     return argument / 2

        >>> assert alt(example)(IOSuccess(1)) == IOSuccess(1)
        >>> assert alt(example)(IOFailure(4)) == IOFailure(2.0)

    Note, that this function works for all containers with ``.alt`` method.
    See :class:`returns.primitives.interfaces.altable.AltableN` for more info.

    """
    @kinded
    def factory(
        container,
    ):
        return container.alt(function)
    return factory
