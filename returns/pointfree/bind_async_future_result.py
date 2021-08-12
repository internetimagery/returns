from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.future import FutureResult
from returns.interfaces.specific.future_result import FutureResultLikeN
from returns.primitives.hkt import Kinded, KindN, kinded

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_FutureResultKind = TypeVar(u'_FutureResultKind', bound=FutureResultLikeN)


def bind_async_future_result(
    function,
):
    u"""
    Compose a container and async function returning ``FutureResult``.

    In other words, it modifies the function
    signature from:
    ``a -> Awaitable[FutureResult[b, c]]``
    to:
    ``Container[a, c] -> Container[b, c]``

    This is how it should be used:

    .. code:: python

      >>> import anyio
      >>> from returns.pointfree import bind_async_future_result
      >>> from returns.future import FutureResult
      >>> from returns.io import IOSuccess, IOFailure

      >>> async def example(argument: int) -> FutureResult[int, str]:
      ...     return FutureResult.from_value(argument + 1)

      >>> assert anyio.run(
      ...     bind_async_future_result(example)(
      ...         FutureResult.from_value(1),
      ...     ).awaitable,
      ... ) == IOSuccess(2)

      >>> assert anyio.run(
      ...     bind_async_future_result(example)(
      ...         FutureResult.from_failure('a'),
      ...     ).awaitable,
      ... ) == IOFailure('a')

    .. currentmodule: returns.primitives.interfaces.specific.future_result

    Note, that this function works
    for all containers with ``.bind_async_future`` method.
    See :class:`~FutureResultLikeN` for more info.

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind_async_future_result(function)
    return factory
