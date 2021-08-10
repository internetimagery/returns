from returns.context import ReaderFutureResult as ReaderFutureResult
from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def bind_context_future_result(function: Callable[[_FirstType], ReaderFutureResult[_UpdatedType, _SecondType, _ThirdType]]) -> Kinded[Callable[[KindN[_ReaderFutureResultLikeKind, _FirstType, _SecondType, _ThirdType]], KindN[_ReaderFutureResultLikeKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
