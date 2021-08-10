from __future__ import absolute_import
from collections import namedtuple
from typing import List, Optional

from mypy.nodes import Context, TempNode
from mypy.types import CallableType
from mypy.types import Type as MypyType
from typing_extensions import final
from itertools import izip

#: Basic struct to represent function arguments.
_FuncArgStruct = namedtuple(u'_FuncArgStruct', (u'name', u'type', u'kind'))


class FuncArg(_FuncArgStruct):
    u"""Representation of function arg with all required fields and methods."""

    name: Optional[unicode]
    type: MypyType  # noqa: WPS125
    kind: int

    def expression(self, context):
        u"""Hack to pass unexisting `Expression` to typechecker."""
        return TempNode(self.type, context=context)

    @classmethod
    def from_callable(cls, function_def):
        u"""Public constructor to create FuncArg lists from callables."""
        parts = izip(
            function_def.arg_names,
            function_def.arg_types,
            function_def.arg_kinds,
        )
        return [cls(*part) for part in parts]

FuncArg = final(FuncArg)
