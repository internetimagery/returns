import abc
from abc import abstractmethod
from returns.interfaces import mappable as mappable
from returns.primitives.hkt import KindN as KindN
from returns.primitives.laws import LawSpecDef as LawSpecDef, Lawful as Lawful
from typing import Any, Callable, Type

class _LawSpec(LawSpecDef):
    def identity_law(container: ApplicativeN[_FirstType, _SecondType, _ThirdType]) -> None: ...
    def interchange_law(raw_value: _FirstType, container: ApplicativeN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], _NewType1]) -> None: ...
    def homomorphism_law(raw_value: _FirstType, container: ApplicativeN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], _NewType1]) -> None: ...
    def composition_law(container: ApplicativeN[_FirstType, _SecondType, _ThirdType], first: Callable[[_FirstType], _NewType1], second: Callable[[_NewType1], _NewType2]) -> None: ...

class ApplicativeN(mappable.MappableN[_FirstType, _SecondType, _ThirdType], Lawful['ApplicativeN[_FirstType, _SecondType, _ThirdType]'], metaclass=abc.ABCMeta):
    @abstractmethod
    def apply(self, container: KindN[_ApplicativeType, Callable[[_FirstType], _UpdatedType], _SecondType, _ThirdType]) -> KindN[_ApplicativeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @classmethod
    @abstractmethod
    def from_value(cls: Type[_ApplicativeType], inner_value: _UpdatedType) -> KindN[_ApplicativeType, _UpdatedType, _SecondType, _ThirdType]: ...

Applicative1: Any
Applicative2: Any
Applicative3: Any
