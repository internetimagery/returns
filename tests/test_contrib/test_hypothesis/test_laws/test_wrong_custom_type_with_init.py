from __future__ import absolute_import
from typing import Callable, TypeVar

import pytest

from returns.contrib.hypothesis.laws import check_all_laws
from returns.interfaces import mappable
from returns.primitives.container import BaseContainer
from returns.primitives.hkt import SupportsKind1

pytestmark = pytest.mark.xfail

_ValueType = TypeVar(u'_ValueType')
_NewValueType = TypeVar(u'_NewValueType')


class _Wrapper(
    BaseContainer,
    SupportsKind1[u'_Wrapper', _ValueType],
    mappable.Mappable1[_ValueType],
):
    _inner_value: _ValueType

    def __init__(self, inner_value):
        super(_Wrapper, self).__init__(inner_value)

    def map(
        self,
        function,
    ):
        return _Wrapper(
            u'wrong-{0}'.format(function(self._inner_value)),  # type: ignore
        )


check_all_laws(_Wrapper, use_init=True)
