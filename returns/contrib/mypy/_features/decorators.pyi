from mypy.nodes import SymbolTableNode as SymbolTableNode
from mypy.plugin import FunctionContext as FunctionContext
from mypy.types import Type as MypyType
from typing import Callable, Optional

def analyze(sym: Optional[SymbolTableNode]) -> Callable[[FunctionContext], MypyType]: ...
