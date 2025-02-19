from __future__ import absolute_import
from typing import TYPE_CHECKING, Callable, TypeVar

from returns.interfaces.specific.reader_future_result import (
    ReaderFutureResultLikeN,
)
from returns.primitives.hkt import Kinded, KindN, kinded

if TYPE_CHECKING:
    from returns.context import ReaderFutureResult  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_ReaderFutureResultLikeKind = TypeVar(
    u'_ReaderFutureResultLikeKind',
    bound=ReaderFutureResultLikeN,
)


def bind_context_future_result(
    function,
):
    u"""
    Lifts function from ``RequiresContextFutureResult`` for better composition.

    In other words, it modifies the function's
    signature from:
    ``a -> RequiresContextFutureResult[env, b, c]``
    to:
    ``Container[env, a, c]`` -> ``Container[env, b, c]``

    .. code:: python

      >>> import anyio
      >>> from returns.context import ReaderFutureResult
      >>> from returns.io import IOSuccess, IOFailure
      >>> from returns.future import FutureResult
      >>> from returns.pointfree import bind_context_future_result

      >>> def function(arg: int) -> ReaderFutureResult[str, int, str]:
      ...     return ReaderFutureResult(
      ...         lambda deps: FutureResult.from_value(len(deps) + arg),
      ...     )

      >>> assert anyio.run(bind_context_future_result(function)(
      ...     ReaderFutureResult.from_value(2),
      ... )('abc').awaitable) == IOSuccess(5)
      >>> assert anyio.run(bind_context_future_result(function)(
      ...     ReaderFutureResult.from_failure(0),
      ... )('abc').awaitable) == IOFailure(0)

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind_context_future_result(function)
    return factory
