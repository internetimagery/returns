from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable, Union

def unify(function: Callable[[_FirstType], KindN[_DiverseFailableKind, _NewFirstType, _NewSecondType, _NewThirdType]]) -> Kinded[Callable[[KindN[_DiverseFailableKind, _FirstType, _SecondType, _ThirdType]], KindN[_DiverseFailableKind, _NewFirstType, Union[_SecondType, _NewSecondType], _NewThirdType]]]: ...
