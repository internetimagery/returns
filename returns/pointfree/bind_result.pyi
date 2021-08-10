from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from returns.result import Result as Result
from typing import Callable

def bind_result(function: Callable[[_FirstType], Result[_UpdatedType, _SecondType]]) -> Kinded[Callable[[KindN[_ResultLikeKind, _FirstType, _SecondType, _ThirdType]], KindN[_ResultLikeKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
