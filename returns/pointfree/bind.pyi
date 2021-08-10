from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def bind(function: Callable[[_FirstType], KindN[_BindableKind, _UpdatedType, _SecondType, _ThirdType]]) -> Kinded[Callable[[KindN[_BindableKind, _FirstType, _SecondType, _ThirdType]], KindN[_BindableKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
