from returns.context import NoDeps as NoDeps
from returns.primitives.hkt import KindN as KindN
from typing import Any, Type

def internal_cond(container_type: Type[_SingleFailableKind], is_success: bool, success_value: _ValueType) -> KindN[_SingleFailableKind, _ValueType, _ErrorType, NoDeps]: ...

cond: Any
