from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Awaitable, Callable

def bind_async(function: Callable[[_FirstType], Awaitable[KindN[_FutureKind, _UpdatedType, _SecondType, _ThirdType]]]) -> Kinded[Callable[[KindN[_FutureKind, _FirstType, _SecondType, _ThirdType]], KindN[_FutureKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
