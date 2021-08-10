from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.interfaces.specific.ioresult import IOResultLikeN
from returns.primitives.hkt import Kind3, Kinded, kinded
from returns.result import Result

_FirstType = TypeVar(u'_FirstType')
_NewFirstType = TypeVar(u'_NewFirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')

_IOResultLikeKind = TypeVar(u'_IOResultLikeKind', bound=IOResultLikeN)


def compose_result(
    function,
):
    u"""
    Composes inner ``Result`` with ``IOResultLike`` returning function.

    Can be useful when you need an access to both states of the result.

    .. code:: python

      >>> from returns.io import IOResult, IOSuccess, IOFailure
      >>> from returns.pointfree import compose_result
      >>> from returns.result import Result

      >>> def modify_string(container: Result[str, str]) -> IOResult[str, str]:
      ...     return IOResult.from_result(
      ...         container.map(str.upper).alt(str.lower),
      ...     )

      >>> assert compose_result(modify_string)(
      ...     IOSuccess('success')
      ... ) == IOSuccess('SUCCESS')
      >>> assert compose_result(modify_string)(
      ...     IOFailure('FAILURE')
      ... ) == IOFailure('failure')

    """
    @kinded
    def factory(
        container,
    ):
        return container.compose_result(function)
    return factory
