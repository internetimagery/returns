from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def map_(function: Callable[[_FirstType], _UpdatedType]) -> Kinded[Callable[[KindN[_MappableKind, _FirstType, _SecondType, _ThirdType]], KindN[_MappableKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
