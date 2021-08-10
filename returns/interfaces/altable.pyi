import abc
from abc import abstractmethod
from returns.primitives.hkt import KindN as KindN
from returns.primitives.laws import LawSpecDef as LawSpecDef, Lawful as Lawful
from typing import Any, Callable

class _LawSpec(LawSpecDef):
    def identity_law(altable: AltableN[_FirstType, _SecondType, _ThirdType]) -> None: ...
    def associative_law(altable: AltableN[_FirstType, _SecondType, _ThirdType], first: Callable[[_SecondType], _NewType1], second: Callable[[_NewType1], _NewType2]) -> None: ...

class AltableN(Lawful['AltableN[_FirstType, _SecondType, _ThirdType]'], metaclass=abc.ABCMeta):
    @abstractmethod
    def alt(self, function: Callable[[_SecondType], _UpdatedType]) -> KindN[_AltableType, _FirstType, _UpdatedType, _ThirdType]: ...

Altable2: Any
Altable3: Any
