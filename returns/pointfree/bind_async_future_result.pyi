from returns.future import FutureResult as FutureResult
from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Awaitable, Callable

def bind_async_future_result(function: Callable[[_FirstType], Awaitable[FutureResult[_UpdatedType, _SecondType]]]) -> Kinded[Callable[[KindN[_FutureResultKind, _FirstType, _SecondType, _ThirdType]], KindN[_FutureResultKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
