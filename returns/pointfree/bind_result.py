from __future__ import absolute_import
from __future__ import annotations

from typing import TYPE_CHECKING, Callable, TypeVar

from returns.interfaces.specific.result import ResultLikeN
from returns.primitives.hkt import Kinded, KindN, kinded

if TYPE_CHECKING:
    from returns.result import Result  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_ResultLikeKind = TypeVar(u'_ResultLikeKind', bound=ResultLikeN)


def bind_result(
    function,
):
    u"""
    Composes successful container with a function that returns a container.

    In other words, it modifies the function's
    signature from:
    ``a -> Result[b, c]``
    to:
    ``Container[a, c] -> Container[b, c]``

    .. code:: python

      >>> from returns.io import IOSuccess
      >>> from returns.context import RequiresContextResult
      >>> from returns.result import Result, Success
      >>> from returns.pointfree import bind_result

      >>> def returns_result(arg: int) -> Result[int, str]:
      ...     return Success(arg + 1)

      >>> bound = bind_result(returns_result)
      >>> assert bound(IOSuccess(1)) == IOSuccess(2)
      >>> assert bound(RequiresContextResult.from_value(1))(...) == Success(2)

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind_result(function)
    return factory
