from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable

def apply(container: KindN[_ApplicativeKind, Callable[[_FirstType], _UpdatedType], _SecondType, _ThirdType]) -> Kinded[Callable[[KindN[_ApplicativeKind, _FirstType, _SecondType, _ThirdType]], KindN[_ApplicativeKind, _UpdatedType, _SecondType, _ThirdType]]]: ...
