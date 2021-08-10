import abc
from abc import abstractmethod
from returns.interfaces import bimappable as bimappable
from returns.primitives.hkt import KindN as KindN
from returns.primitives.laws import LawSpecDef as LawSpecDef, Lawful as Lawful
from typing import Any

class _LawSpec(LawSpecDef):
    def double_swap_law(container: SwappableN[_FirstType, _SecondType, _ThirdType]) -> None: ...

class SwappableN(bimappable.BiMappableN[_FirstType, _SecondType, _ThirdType], Lawful['SwappableN[_FirstType, _SecondType, _ThirdType]'], metaclass=abc.ABCMeta):
    @abstractmethod
    def swap(self) -> KindN[_SwappableType, _SecondType, _FirstType, _ThirdType]: ...

Swappable2: Any
Swappable3: Any
