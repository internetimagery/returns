from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from returns.result import Result as Result
from typing import Callable

def managed(use: Callable[[_FirstType], KindN[_IOResultLikeType, _UpdatedType, _SecondType, _ThirdType]], release: Callable[[_FirstType, Result[_UpdatedType, _SecondType]], KindN[_IOResultLikeType, None, _SecondType, _ThirdType]]) -> Kinded[Callable[[KindN[_IOResultLikeType, _FirstType, _SecondType, _ThirdType]], KindN[_IOResultLikeType, _UpdatedType, _SecondType, _ThirdType]]]: ...
