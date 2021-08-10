from mypy.plugin import FunctionContext as FunctionContext
from mypy.types import Type as MypyType

def analyze(ctx: FunctionContext) -> MypyType: ...
