import abc
from returns.interfaces import applicative as applicative, bindable as bindable
from returns.primitives.hkt import KindN as KindN
from returns.primitives.laws import LawSpecDef as LawSpecDef, Lawful as Lawful
from typing import Any, Callable

class _LawSpec(LawSpecDef):
    def left_identity_law(raw_value: _FirstType, container: ContainerN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], KindN[ContainerN, _NewType1, _SecondType, _ThirdType]]) -> None: ...
    def right_identity_law(container: ContainerN[_FirstType, _SecondType, _ThirdType]) -> None: ...
    def associative_law(container: ContainerN[_FirstType, _SecondType, _ThirdType], first: Callable[[_FirstType], KindN[ContainerN, _NewType1, _SecondType, _ThirdType]], second: Callable[[_NewType1], KindN[ContainerN, _NewType2, _SecondType, _ThirdType]]) -> None: ...

class ContainerN(applicative.ApplicativeN[_FirstType, _SecondType, _ThirdType], bindable.BindableN[_FirstType, _SecondType, _ThirdType], Lawful['ContainerN[_FirstType, _SecondType, _ThirdType]'], metaclass=abc.ABCMeta): ...

Container1: Any
Container2: Any
Container3: Any
