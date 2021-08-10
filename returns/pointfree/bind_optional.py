from __future__ import absolute_import
from typing import Callable, Optional, TypeVar

from returns.interfaces.specific.maybe import MaybeLikeN
from returns.primitives.hkt import Kinded, KindN, kinded

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_MaybeLikeKind = TypeVar(u'_MaybeLikeKind', bound=MaybeLikeN)


def bind_optional(
    function,
):
    u"""
    Binds a function returning optional value over a container.

    In other words, it modifies the function's
    signature from:
    ``a -> Optional[b]``
    to:
    ``Container[a] -> Container[b]``

    .. code:: python

      >>> from typing import Optional
      >>> from returns.pointfree import bind_optional
      >>> from returns.maybe import Some, Nothing

      >>> def example(argument: int) -> Optional[int]:
      ...     return argument + 1 if argument > 0 else None

      >>> assert bind_optional(example)(Some(1)) == Some(2)
      >>> assert bind_optional(example)(Some(0)) == Nothing
      >>> assert bind_optional(example)(Nothing) == Nothing

    Note, that this function works
    for all containers with ``.bind_optional`` method.
    See :class:`returns.primitives.interfaces.specific.maybe._MaybeLikeKind`
    for more info.

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind_optional(function)
    return factory
