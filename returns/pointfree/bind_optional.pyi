from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable, Optional

def bind_optional(function: Callable[[_FirstType], Optional[_UpdatedType]]) -> Kinded[Callable[[KindN[_MaybeLikeKind, _FirstType, _SecondType, _ThirdType]], KindN[_MaybeLikeKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
