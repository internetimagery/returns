from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.interfaces.bindable import BindableN
from returns.primitives.hkt import Kinded, KindN, kinded

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_BindableKind = TypeVar(u'_BindableKind', bound=BindableN)


def bind(
    function,
):
    u"""
    Turns function's input parameter from a regular value to a container.

    In other words, it modifies the function
    signature from:
    ``a -> Container[b]``
    to:
    ``Container[a] -> Container[b]``

    Similar to :func:`returns.pointfree.lash`,
    but works for successful containers.
    This is how it should be used:

    .. code:: python

      >>> from returns.pointfree import bind
      >>> from returns.maybe import Maybe, Some, Nothing

      >>> def example(argument: int) -> Maybe[int]:
      ...     return Some(argument + 1)

      >>> assert bind(example)(Some(1)) == Some(2)
      >>> assert bind(example)(Nothing) == Nothing

    Note, that this function works for all containers with ``.bind`` method.
    See :class:`returns.primitives.interfaces.bindable.BindableN` for more info.

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind(function)
    return factory
