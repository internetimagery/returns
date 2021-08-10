from returns.primitives.hkt import Kind3 as Kind3, Kinded as Kinded
from returns.result import Result as Result
from typing import Callable

def compose_result(function: Callable[[Result[_FirstType, _SecondType]], Kind3[_IOResultLikeKind, _NewFirstType, _SecondType, _ThirdType]]) -> Kinded[Callable[[Kind3[_IOResultLikeKind, _FirstType, _SecondType, _ThirdType]], Kind3[_IOResultLikeKind, _NewFirstType, _SecondType, _ThirdType]]]: ...
