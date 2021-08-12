from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.interfaces.specific.future import FutureLikeN
from returns.primitives.hkt import Kinded, KindN, kinded

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_FutureKind = TypeVar(u'_FutureKind', bound=FutureLikeN)


def bind_awaitable(
    function,
):
    u"""
    Composes a container a regular ``async`` function.

    This function should return plain, non-container value.

    In other words, it modifies the function's
    signature from:
    ``a -> Awaitable[b]``
    to:
    ``Container[a] -> Container[b]``

    This is how it should be used:

    .. code:: python

        >>> import anyio
        >>> from returns.future import Future
        >>> from returns.io import IO
        >>> from returns.pointfree import bind_awaitable

        >>> async def coroutine(x: int) -> int:
        ...    return x + 1

        >>> assert anyio.run(
        ...     bind_awaitable(coroutine)(Future.from_value(1)).awaitable,
        ... ) == IO(2)

    Note, that this function works
    for all containers with ``.bind_awaitable`` method.
    See :class:`returns.primitives.interfaces.specific.future.FutureLikeN`
    for more info.

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind_awaitable(function)
    return factory
