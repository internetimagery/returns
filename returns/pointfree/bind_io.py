from __future__ import absolute_import

from typing import TYPE_CHECKING, Callable, TypeVar

from returns.interfaces.specific.io import IOLikeN
from returns.primitives.hkt import Kinded, KindN, kinded

if TYPE_CHECKING:
    from returns.io import IO  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType', contravariant=True)
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType', contravariant=True)
_UpdatedType = TypeVar(u'_UpdatedType', covariant=True)

_IOLikeKind = TypeVar(u'_IOLikeKind', bound=IOLikeN)


def bind_io(
    function,
):
    u"""
    Composes successful container with a function that returns a container.

    In other words, it modifies the function's
    signature from:
    ``a -> IO[b]``
    to:
    ``Container[a, c] -> Container[b, c]``

    .. code:: python

      >>> from returns.io import IOSuccess, IOFailure
      >>> from returns.io import IO
      >>> from returns.pointfree import bind_io

      >>> def returns_io(arg: int) -> IO[int]:
      ...     return IO(arg + 1)

      >>> bound = bind_io(returns_io)
      >>> assert bound(IO(1)) == IO(2)
      >>> assert bound(IOSuccess(1)) == IOSuccess(2)
      >>> assert bound(IOFailure(1)) == IOFailure(1)

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind_io(function)
    return factory
