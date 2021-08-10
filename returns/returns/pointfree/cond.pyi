from returns.context import NoDeps as NoDeps
from returns.primitives.hkt import KindN as KindN, Kinded as Kinded
from typing import Callable, Type

def cond(container_type: Type[_SingleFailableKind], success_value: _ValueType) -> Kinded[Callable[[bool], KindN[_SingleFailableKind, _ValueType, _ErrorType, NoDeps]]]: ...
