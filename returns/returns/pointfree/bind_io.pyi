from returns.io import IO as IO
from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def bind_io(function: Callable[[_FirstType], IO[_UpdatedType]]) -> Kinded[Callable[[KindN[_IOLikeKind, _FirstType, _SecondType, _ThirdType]], KindN[_IOLikeKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
