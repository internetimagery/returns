from returns.io import IOResult as IOResult
from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def bind_ioresult(function: Callable[[_FirstType], IOResult[_UpdatedType, _SecondType]]) -> Kinded[Callable[[KindN[_IOResultLikeKind, _FirstType, _SecondType, _ThirdType]], KindN[_IOResultLikeKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
