from __future__ import absolute_import
from typing import Callable, TypeVar

from returns.contrib.hypothesis.laws import check_all_laws
from returns.interfaces import applicative
from returns.primitives.container import BaseContainer
from returns.primitives.hkt import Kind1, SupportsKind1

_ValueType = TypeVar(u'_ValueType')
_NewValueType = TypeVar(u'_NewValueType')


class _Wrapper(
    BaseContainer,
    SupportsKind1[u'_Wrapper', _ValueType],
    applicative.Applicative1[_ValueType],
):
    _inner_value: _ValueType

    def __init__(self, inner_value):
        super(_Wrapper, self).__init__(inner_value)

    def map(
        self,
        function,
    ):
        return _Wrapper(function(self._inner_value))

    def apply(
        self,
        container,
    ):
        function = container._inner_value  # noqa: WPS437
        return _Wrapper(function(self._inner_value))

    @classmethod
    def from_value(
        cls,
        inner_value,
    ):
        return _Wrapper(inner_value)


check_all_laws(_Wrapper)
