from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.interfaces.applicative import ApplicativeN
from returns.primitives.hkt import Kinded, KindN, kinded

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_ApplicativeKind = TypeVar(u'_ApplicativeKind', bound=ApplicativeN)


def apply(
    container,
):
    u"""
    Turns container containing a function into a callable.

    In other words, it modifies the function
    signature from:
    ``Container[a -> b]``
    to:
    ``Container[a] -> Container[b]``

    This is how it should be used:

    .. code:: python

      >>> from returns.pointfree import apply
      >>> from returns.maybe import Some, Nothing

      >>> def example(argument: int) -> int:
      ...     return argument + 1

      >>> assert apply(Some(example))(Some(1)) == Some(2)
      >>> assert apply(Some(example))(Nothing) == Nothing
      >>> assert apply(Nothing)(Some(1)) == Nothing
      >>> assert apply(Nothing)(Nothing) == Nothing

    Note, that this function works for all containers with ``.apply`` method.
    See :class:`returns.interfaces.applicative.ApplicativeN` for more info.

    """
    @kinded
    def factory(
        other,
    ):
        return other.apply(container)
    return factory
