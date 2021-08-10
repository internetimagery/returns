from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.interfaces.mappable import MappableN
from returns.primitives.hkt import Kinded, KindN, kinded

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_MappableKind = TypeVar(u'_MappableKind', bound=MappableN)


def map_(
    function,
):
    u"""
    Lifts function to be wrapped in a container for better composition.

    In other words, it modifies the function's
    signature from:
    ``a -> b``
    to: ``Container[a] -> Container[b]``

    This is how it should be used:

    .. code:: python

        >>> from returns.io import IO
        >>> from returns.pointfree import map_

        >>> def example(argument: int) -> float:
        ...     return argument / 2

        >>> assert map_(example)(IO(1)) == IO(0.5)

    Note, that this function works for all containers with ``.map`` method.
    See :class:`returns.primitives.interfaces.mappable.MappableN` for more info.

    See also:
        - https://wiki.haskell.org/Lifting

    """
    @kinded
    def factory(
        container,
    ):
        return container.map(function)
    return factory
