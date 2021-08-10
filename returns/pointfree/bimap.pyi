from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def bimap(on_first: Callable[[_FirstType], _UpdatedType1], on_second: Callable[[_SecondType], _UpdatedType2]) -> Kinded[Callable[[KindN[_BiMappableKind, _FirstType, _SecondType, _ThirdType]], KindN[_BiMappableKind, _UpdatedType1, _UpdatedType2, _ThirdType]]]: ...
