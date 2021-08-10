import abc
from abc import abstractmethod
from returns.interfaces import container as _container, lashable as lashable, swappable as swappable
from returns.primitives.hkt import KindN as KindN
from returns.primitives.laws import LawSpecDef as LawSpecDef, Lawful as Lawful
from typing import Any, Callable, Type

class _FailableLawSpec(LawSpecDef):
    def lash_short_circuit_law(raw_value: _FirstType, container: FailableN[_FirstType, _SecondType, _ThirdType], function: Callable[[_SecondType], KindN[FailableN, _FirstType, _NewFirstType, _ThirdType]]) -> None: ...

class FailableN(_container.ContainerN[_FirstType, _SecondType, _ThirdType], lashable.LashableN[_FirstType, _SecondType, _ThirdType], Lawful['FailableN[_FirstType, _SecondType, _ThirdType]'], metaclass=abc.ABCMeta): ...

Failable2: Any
Failable3: Any

class _SingleFailableLawSpec(LawSpecDef):
    def map_short_circuit_law(container: SingleFailableN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], _NewFirstType]) -> None: ...
    def bind_short_circuit_law(container: SingleFailableN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], KindN[SingleFailableN, _NewFirstType, _SecondType, _ThirdType]]) -> None: ...
    def apply_short_circuit_law(container: SingleFailableN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], _NewFirstType]) -> None: ...

class SingleFailableN(FailableN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def empty(self) -> SingleFailableN[_FirstType, _SecondType, _ThirdType]: ...

SingleFailable2: Any
SingleFailable3: Any

class _DiverseFailableLawSpec(LawSpecDef):
    def map_short_circuit_law(raw_value: _SecondType, container: DiverseFailableN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], _NewFirstType]) -> None: ...
    def bind_short_circuit_law(raw_value: _SecondType, container: DiverseFailableN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], KindN[DiverseFailableN, _NewFirstType, _SecondType, _ThirdType]]) -> None: ...
    def apply_short_circuit_law(raw_value: _SecondType, container: DiverseFailableN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], _NewFirstType]) -> None: ...
    def alt_short_circuit_law(raw_value: _SecondType, container: DiverseFailableN[_FirstType, _SecondType, _ThirdType], function: Callable[[_SecondType], _NewFirstType]) -> None: ...

class DiverseFailableN(FailableN[_FirstType, _SecondType, _ThirdType], swappable.SwappableN[_FirstType, _SecondType, _ThirdType], Lawful['DiverseFailableN[_FirstType, _SecondType, _ThirdType]'], metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def from_failure(cls: Type[_DiverseFailableType], inner_value: _UpdatedType) -> KindN[_DiverseFailableType, _FirstType, _UpdatedType, _ThirdType]: ...

DiverseFailable2: Any
DiverseFailable3: Any
