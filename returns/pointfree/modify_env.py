from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.interfaces.specific.reader import ReaderLike2, ReaderLike3
from returns.primitives.hkt import Kind2, Kind3, Kinded, kinded

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_Reader2Kind = TypeVar(u'_Reader2Kind', bound=ReaderLike2)
_Reader3Kind = TypeVar(u'_Reader3Kind', bound=ReaderLike3)


def modify_env2(
    function,
):
    u"""
    Modifies the second type argument of a ``ReaderLike2``.

    In other words, it modifies the function's
    signature from:
    ``a -> b``
    to:
    ``Container[x, a] -> Container[x, b]``

    .. code:: python

      >>> from returns.pointfree import modify_env2
      >>> from returns.context import RequiresContext

      >>> def multiply(arg: int) -> RequiresContext[int, int]:
      ...     return RequiresContext(lambda deps: arg * deps)

      >>> assert modify_env2(int)(multiply(3))('4') == 12

    Note, that this function works with only ``Kind2`` containers
    with ``.modify_env`` method.
    See :class:`returns.primitives.interfaces.specific.reader.ReaderLike2`
    for more info.

    """
    @kinded
    def factory(
        container,
    ):
        return container.modify_env(function)
    return factory


def modify_env3(
    function,
):
    u"""
    Modifies the third type argument of a ``ReaderLike3``.

    In other words, it modifies the function's
    signature from: ``a -> b``
    to: ``Container[x, a] -> Container[x, b]``

    .. code:: python

      >>> from returns.pointfree import modify_env
      >>> from returns.context import RequiresContextResultE
      >>> from returns.result import Success, safe

      >>> def divide(arg: int) -> RequiresContextResultE[float, int]:
      ...     return RequiresContextResultE(safe(lambda deps: arg / deps))

      >>> assert modify_env(int)(divide(3))('2') == Success(1.5)
      >>> assert modify_env(int)(divide(3))('0').failure()

    Note, that this function works with only ``Kind3`` containers
    with ``.modify_env`` method.
    See :class:`returns.primitives.interfaces.specific.reader.ReaderLike3`
    for more info.

    """
    @kinded
    def factory(
        container,
    ):
        return container.modify_env(function)
    return factory


#: Useful alias for :func:`~modify_env3`.
modify_env = modify_env3
