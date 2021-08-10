from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Awaitable, Callable

def bind_awaitable(function: Callable[[_FirstType], Awaitable[_UpdatedType]]) -> Kinded[Callable[[KindN[_FutureKind, _FirstType, _SecondType, _ThirdType]], KindN[_FutureKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
