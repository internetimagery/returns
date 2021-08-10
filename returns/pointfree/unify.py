from __future__ import absolute_import
from typing import Callable, TypeVar, Union

from returns.interfaces.failable import DiverseFailableN
from returns.primitives.hkt import Kinded, KindN, kinded

_FirstType = TypeVar(u'_FirstType')
_NewFirstType = TypeVar(u'_NewFirstType')
_SecondType = TypeVar(u'_SecondType')
_NewSecondType = TypeVar(u'_NewSecondType')
_ThirdType = TypeVar(u'_ThirdType')
_NewThirdType = TypeVar(u'_NewThirdType')

_DiverseFailableKind = TypeVar(u'_DiverseFailableKind', bound=DiverseFailableN)


def unify(  # noqa: WPS234
    function,
):
    u"""
    Composes successful container with a function that returns a container.

    Similar to :func:`~returns.pointfree.bind` but has different type.
    It returns ``Result[ValueType, Union[OldErrorType, NewErrorType]]``
    instead of ``Result[ValueType, OldErrorType]``.

    So, it can be more useful in some situations.
    Probably with specific exceptions.

    .. code:: python

      >>> from returns.methods import cond
      >>> from returns.pointfree import unify
      >>> from returns.result import Result, Success, Failure

      >>> def bindable(arg: int) -> Result[int, int]:
      ...     return cond(Result, arg % 2 == 0, arg + 1, arg - 1)

      >>> assert unify(bindable)(Success(2)) == Success(3)
      >>> assert unify(bindable)(Success(1)) == Failure(0)
      >>> assert unify(bindable)(Failure(42)) == Failure(42)

    """
    @kinded
    def factory(
        container,
    ):
        return container.bind(function)  # type: ignore
    return factory
