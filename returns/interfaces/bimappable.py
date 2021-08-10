from __future__ import absolute_import
from typing import NoReturn, TypeVar

from returns.interfaces import altable, mappable

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')


class BiMappableN(
    mappable.MappableN[_FirstType, _SecondType, _ThirdType],
    altable.AltableN[_FirstType, _SecondType, _ThirdType],
):
    u"""
    Allows to change both types of a container at the same time.

    Uses ``.map`` to change first type and ``.alt`` to change second type.

    See also:
        - https://typelevel.org/cats/typeclasses/bifunctor.html

    """


#: Type alias for kinds with two type arguments.
BiMappable2 = BiMappableN[_FirstType, _SecondType, NoReturn]

#: Type alias for kinds with three type arguments.
BiMappable3 = BiMappableN[_FirstType, _SecondType, _ThirdType]
