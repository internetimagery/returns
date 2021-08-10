from returns.context import ReaderResult as ReaderResult
from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def bind_context_result(function: Callable[[_FirstType], ReaderResult[_UpdatedType, _SecondType, _ThirdType]]) -> Kinded[Callable[[KindN[_ReaderResultLikeKind, _FirstType, _SecondType, _ThirdType]], KindN[_ReaderResultLikeKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
