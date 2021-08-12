from __future__ import absolute_import

from typing import TYPE_CHECKING, Callable, TypeVar

from returns.interfaces.specific.reader import ReaderLike2, ReaderLike3
from returns.primitives.hkt import Kind2, Kind3, Kinded, kinded

if TYPE_CHECKING:
    from returns.context import RequiresContext  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_Reader2Kind = TypeVar(u'_Reader2Kind', bound=ReaderLike2)
_Reader3Kind = TypeVar(u'_Reader3Kind', bound=ReaderLike3)


def bind_context2(
    function,
):
    u"""
    Composes successful container with a function that returns a container.

    In other words, it modifies the function's
    signature from:
    ``a -> RequresContext[b, c]``
    to:
    ``Container[a, c] -> Container[b, c]``

    .. code:: python

      >>> from returns.pointfree import bind_context2
      >>> from returns.context import Reader

      >>> def example(argument: int) -> Reader[int, int]:
      ...     return Reader(lambda deps: argument + deps)

      >>> assert bind_context2(example)(Reader.from_value(2))(3) == 5

    Note, that this function works with only ``Kind2`` containers
    with ``.bind_context`` method.
    See :class:`returns.primitives.interfaces.specific.reader.ReaderLike2`
    for more info.

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind_context(function)
    return factory


def bind_context3(
    function,
):
    u"""
    Composes successful container with a function that returns a container.

    In other words, it modifies the function's
    signature from: ``a -> RequresContext[b, c]``
    to: ``Container[a, c] -> Container[b, c]``

    .. code:: python

        >>> from returns.context import RequiresContext, RequiresContextResult
        >>> from returns.result import Success, Failure
        >>> from returns.pointfree import bind_context

        >>> def function(arg: int) -> RequiresContext[str, int]:
        ...     return RequiresContext(lambda deps: len(deps) + arg)

        >>> assert bind_context(function)(
        ...     RequiresContextResult.from_value(2),
        ... )('abc') == Success(5)
        >>> assert bind_context(function)(
        ...     RequiresContextResult.from_failure(0),
        ... )('abc') == Failure(0)

    Note, that this function works with only ``Kind3`` containers
    with ``.bind_context`` method.
    See :class:`returns.primitives.interfaces.specific.reader.ReaderLike3`
    for more info.

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind_context(function)
    return factory


#: Useful alias for :func:`~bind_context3`.
bind_context = bind_context3
