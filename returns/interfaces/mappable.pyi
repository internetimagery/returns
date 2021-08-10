import abc
from abc import abstractmethod
from returns.primitives.hkt import KindN as KindN
from returns.primitives.laws import LawSpecDef as LawSpecDef, Lawful as Lawful
from typing import Any, Callable

class _LawSpec(LawSpecDef):
    def identity_law(mappable: MappableN[_FirstType, _SecondType, _ThirdType]) -> None: ...
    def associative_law(mappable: MappableN[_FirstType, _SecondType, _ThirdType], first: Callable[[_FirstType], _NewType1], second: Callable[[_NewType1], _NewType2]) -> None: ...

class MappableN(Lawful['MappableN[_FirstType, _SecondType, _ThirdType]'], metaclass=abc.ABCMeta):
    @abstractmethod
    def map(self, function: Callable[[_FirstType], _UpdatedType]) -> KindN[_MappableType, _UpdatedType, _SecondType, _ThirdType]: ...

Mappable1: Any
Mappable2: Any
Mappable3: Any
