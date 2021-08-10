from __future__ import absolute_import
from typing import Union

from mypy.plugin import FunctionContext, MethodContext

#: We treat them equally when working with functions or methods.
CallableContext = Union[
    FunctionContext,
    MethodContext,
]
