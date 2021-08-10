from collections import namedtuple
from mypy.nodes import Context as Context, TempNode as TempNode
from mypy.types import CallableType as CallableType, Type as MypyType
from typing import Any, List, Optional

_FuncArgStruct = namedtuple('_FuncArgStruct', ['name', 'type', 'kind'])

class FuncArg(_FuncArgStruct):
    name: Optional[str]
    type: MypyType
    kind: int
    def expression(self, context: Context) -> TempNode: ...
    @classmethod
    def from_callable(cls: Any, function_def: CallableType) -> List[FuncArg]: ...
