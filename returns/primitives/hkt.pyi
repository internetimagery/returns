import abc
from typing import Any, Callable

class KindN:
    def __getattr__(self, attrname: str) -> Any: ...

Kind1: Any
Kind2: Any
Kind3: Any

class SupportsKindN(KindN[_InstanceType, _TypeArgType1, _TypeArgType2, _TypeArgType3]):
    __getattr__: None

SupportsKind1: Any
SupportsKind2: Any
SupportsKind3: Any

def dekind(kind: KindN[_InstanceType, _TypeArgType1, _TypeArgType2, _TypeArgType3]) -> _InstanceType: ...

class Kinded(metaclass=abc.ABCMeta):
    __call__: _FunctionDefType
    def __get__(self, instance: _UpdatedType, type_: Any) -> Callable[..., _UpdatedType]: ...

def kinded(function: _FunctionType) -> Kinded[_FunctionType]: ...
