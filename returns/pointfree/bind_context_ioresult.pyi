from returns.context import ReaderIOResult as ReaderIOResult
from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def bind_context_ioresult(function: Callable[[_FirstType], ReaderIOResult[_UpdatedType, _SecondType, _ThirdType]]) -> Kinded[Callable[[KindN[_ReaderIOResultLikeKind, _FirstType, _SecondType, _ThirdType]], KindN[_ReaderIOResultLikeKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
