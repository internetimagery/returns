from returns.context import RequiresContext as RequiresContext
from returns.primitives.hkt import Kind2 as Kind2, Kind3 as Kind3, Kinded as Kinded
from typing import Callable

def bind_context2(function: Callable[[_FirstType], RequiresContext[_UpdatedType, _SecondType]]) -> Kinded[Callable[[Kind2[_Reader2Kind, _FirstType, _SecondType]], Kind2[_Reader2Kind, _UpdatedType, _SecondType]]]: ...
def bind_context3(function: Callable[[_FirstType], RequiresContext[_UpdatedType, _ThirdType]]) -> Kinded[Callable[[Kind3[_Reader3Kind, _FirstType, _SecondType, _ThirdType]], Kind3[_Reader3Kind, _UpdatedType, _SecondType, _ThirdType]]]: ...
bind_context = bind_context3
