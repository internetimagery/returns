from __future__ import absolute_import

from typing import TYPE_CHECKING, Callable, TypeVar

from returns.interfaces.specific.reader_ioresult import ReaderIOResultLikeN
from returns.primitives.hkt import Kinded, KindN, kinded

if TYPE_CHECKING:
    from returns.context import ReaderIOResult  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_ReaderIOResultLikeKind = TypeVar(
    u'_ReaderIOResultLikeKind',
    bound=ReaderIOResultLikeN,
)


def bind_context_ioresult(
    function,
):
    u"""
    Lifts function from ``RequiresContextIOResult`` for better composition.

    In other words, it modifies the function's
    signature from:
    ``a -> RequiresContextIOResult[env, b, c]``
    to:
    ``Container[env, a, c]`` -> ``Container[env, b, c]``

    .. code:: python

      >>> import anyio
      >>> from returns.context import (
      ...     RequiresContextFutureResult,
      ...     RequiresContextIOResult,
      ... )
      >>> from returns.io import IOSuccess, IOFailure
      >>> from returns.pointfree import bind_context_ioresult

      >>> def function(arg: int) -> RequiresContextIOResult[str, int, str]:
      ...     return RequiresContextIOResult(
      ...         lambda deps: IOSuccess(len(deps) + arg),
      ...     )

      >>> assert anyio.run(bind_context_ioresult(function)(
      ...     RequiresContextFutureResult.from_value(2),
      ... )('abc').awaitable) == IOSuccess(5)
      >>> assert anyio.run(bind_context_ioresult(function)(
      ...     RequiresContextFutureResult.from_failure(0),
      ... )('abc').awaitable) == IOFailure(0)

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind_context_ioresult(function)
    return factory
