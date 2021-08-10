from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.future import Future
from returns.interfaces.specific.future import FutureLikeN
from returns.primitives.hkt import Kinded, KindN, kinded

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_FutureKind = TypeVar(u'_FutureKind', bound=FutureLikeN)


def bind_future(
    function,
):
    u"""
    Compose a container and sync function returning ``Future``.

    In other words, it modifies the function
    signature from:
    ``a -> Future[b]``
    to:
    ``Container[a] -> Container[b]``

    Similar to :func:`returns.pointfree.lash`,
    but works for successful containers.
    This is how it should be used:

    .. code:: python

      >>> import anyio
      >>> from returns.pointfree import bind_future
      >>> from returns.future import Future
      >>> from returns.io import IO

      >>> def example(argument: int) -> Future[int]:
      ...     return Future.from_value(argument + 1)

      >>> assert anyio.run(
      ...     bind_future(example)(Future.from_value(1)).awaitable,
      ... ) == IO(2)

    Note, that this function works
    for all containers with ``.bind_future`` method.
    See :class:`returns.primitives.interfaces.specific.future.FutureLikeN`
    for more info.

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind_future(function)
    return factory
