from __future__ import absolute_import

from typing import TYPE_CHECKING, Callable, TypeVar

from returns.interfaces.specific.ioresult import IOResultLikeN
from returns.primitives.hkt import Kinded, KindN, kinded

if TYPE_CHECKING:
    from returns.io import IOResult  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_IOResultLikeKind = TypeVar(u'_IOResultLikeKind', bound=IOResultLikeN)


def bind_ioresult(
    function,
):
    u"""
    Composes successful container with a function that returns a container.

    In other words, it modifies the function's
    signature from:
    ``a -> IOResult[b, c]``
    to:
    ``Container[a, c] -> Container[b, c]``

    .. code:: python

      >>> from returns.io import IOResult, IOSuccess
      >>> from returns.context import RequiresContextIOResult
      >>> from returns.pointfree import bind_ioresult

      >>> def returns_ioresult(arg: int) -> IOResult[int, str]:
      ...     return IOSuccess(arg + 1)

      >>> bound = bind_ioresult(returns_ioresult)
      >>> assert bound(IOSuccess(1)) == IOSuccess(2)
      >>> assert bound(
      ...     RequiresContextIOResult.from_value(1),
      ... )(...) == IOSuccess(2)

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind_ioresult(function)
    return factory
