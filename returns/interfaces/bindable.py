from __future__ import absolute_import
from abc import abstractmethod
from typing import Callable, Generic, NoReturn, TypeVar

from returns.primitives.hkt import KindN

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_BindableType = TypeVar(u'_BindableType', bound=u'BindableN')


class BindableN(Generic[_FirstType, _SecondType, _ThirdType]):
    u"""
    Represents a "context" in which calculations can be executed.

    ``Bindable`` allows you to bind together
    a series of calculations while maintaining
    the context of that specific container.

    In contrast to :class:`returns.interfaces.lashable.LashableN`,
    works with the first type argument.
    """

    @abstractmethod
    def bind(
        self,
        function,
    ):
        u"""
        Applies 'function' to the result of a previous calculation.

        And returns a new container.
        """


#: Type alias for kinds with one type argument.
Bindable1 = BindableN[_FirstType, NoReturn, NoReturn]

#: Type alias for kinds with two type arguments.
Bindable2 = BindableN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
Bindable3 = BindableN[_FirstType, _SecondType, _ThirdType]
