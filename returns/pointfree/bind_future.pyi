from returns.future import Future as Future
from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def bind_future(function: Callable[[_FirstType], Future[_UpdatedType]]) -> Kinded[Callable[[KindN[_FutureKind, _FirstType, _SecondType, _ThirdType]], KindN[_FutureKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
