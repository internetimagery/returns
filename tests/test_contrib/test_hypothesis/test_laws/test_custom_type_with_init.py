from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.contrib.hypothesis.laws import check_all_laws
from returns.interfaces import equable, mappable
from returns.primitives.container import BaseContainer, container_equality
from returns.primitives.hkt import SupportsKind1

_ValueType = TypeVar(u'_ValueType')
_NewValueType = TypeVar(u'_NewValueType')


class _Wrapper(
    BaseContainer,
    SupportsKind1[u'_Wrapper', _ValueType],
    mappable.Mappable1[_ValueType],
    equable.Equable,
):
    _inner_value: _ValueType

    def __init__(self, inner_value):
        super(_Wrapper, self).__init__(inner_value)

    equals = container_equality

    def map(
        self,
        function,
    ):
        return _Wrapper(function(self._inner_value))


check_all_laws(_Wrapper, use_init=True)
