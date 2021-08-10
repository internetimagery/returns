from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def alt(function: Callable[[_SecondType], _UpdatedType]) -> Kinded[Callable[[KindN[_AltableKind, _FirstType, _SecondType, _ThirdType]], KindN[_AltableKind, _FirstType, _UpdatedType, _ThirdType]]]: ...
