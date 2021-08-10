from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def lash(function: Callable[[_SecondType], KindN[_LashableKind, _FirstType, _UpdatedType, _ThirdType]]) -> Kinded[Callable[[KindN[_LashableKind, _FirstType, _SecondType, _ThirdType]], KindN[_LashableKind, _FirstType, _UpdatedType, _ThirdType]]]: ...
