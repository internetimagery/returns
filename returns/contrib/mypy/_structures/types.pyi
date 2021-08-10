from mypy.plugin import FunctionContext, MethodContext
from typing import Union

CallableContext = Union[FunctionContext, MethodContext]
