from __future__ import absolute_import

from abc import abstractmethod
from typing import TYPE_CHECKING, Callable, NoReturn, Type, TypeVar

from returns.interfaces import container, equable
from returns.primitives.hkt import KindN

if TYPE_CHECKING:
    from returns.io import IO  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_IOLikeType = TypeVar(u'_IOLikeType', bound=u'IOLikeN')


class IOLikeN(container.ContainerN[_FirstType, _SecondType, _ThirdType]):
    u"""
    Represents interface for types that looks like fearless ``IO``.

    This type means that ``IO`` cannot fail. Like random numbers, date, etc.
    Don't use this type for ``IO`` that can. Instead, use
    :class:`returns.interfaces.specific.ioresult.IOResultBasedN` type.

    """

    @abstractmethod
    def bind_io(
        self,
        function,
    ):
        u"""Allows to apply a wrapped function over a container."""

    @classmethod
    @abstractmethod
    def from_io(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Unit method to create new containers from successful ``IO``."""


#: Type alias for kinds with one type argument.
IOLike1 = IOLikeN[_FirstType, NoReturn, NoReturn]

#: Type alias for kinds with two type arguments.
IOLike2 = IOLikeN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
IOLike3 = IOLikeN[_FirstType, _SecondType, _ThirdType]


class IOBasedN(
    IOLikeN[_FirstType, _SecondType, _ThirdType],
    equable.Equable,
):
    u"""
    Represents the base interface for types that do fearless ``IO``.

    This type means that ``IO`` cannot fail. Like random numbers, date, etc.
    Don't use this type for ``IO`` that can. Instead, use
    :class:`returns.interfaces.specific.ioresult.IOResultBasedN` type.

    This interface also supports direct comparison of two values.
    While ``IOLikeN`` is different. It can be lazy and cannot be compared.

    """


#: Type alias for kinds with one type argument.
IOBased1 = IOBasedN[_FirstType, NoReturn, NoReturn]

#: Type alias for kinds with two type arguments.
IOBased2 = IOBasedN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
IOBased3 = IOBasedN[_FirstType, _SecondType, _ThirdType]
