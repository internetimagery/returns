from __future__ import absolute_import
from abc import abstractmethod
from typing import Callable, Generic, NoReturn, TypeVar

from returns.primitives.hkt import KindN

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_LashableType = TypeVar(u'_LashableType', bound=u'LashableN')


class LashableN(Generic[_FirstType, _SecondType, _ThirdType]):
    u"""
    Represents a "context" in which calculations can be executed.

    ``Rescueable`` allows you to bind together
    a series of calculations while maintaining
    the context of that specific container.

    In contrast to :class:`returns.interfaces.bindable.BinbdaleN`,
    works with the second type value.
    """

    @abstractmethod
    def lash(
        self,
        function,
    ):
        u"""
        Applies 'function' to the result of a previous calculation.

        And returns a new container.
        """


#: Type alias for kinds with two type arguments.
Lashable2 = LashableN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
Lashable3 = LashableN[_FirstType, _SecondType, _ThirdType]
