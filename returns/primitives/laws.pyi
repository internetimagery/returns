from returns.primitives.types import Immutable as Immutable
from typing import Any, Callable, Dict, Sequence, Type

law_definition = staticmethod

class Law(Immutable):
    definition: Callable
    def __init__(self, function: Any) -> None: ...
    @property
    def name(self) -> str: ...

class Law1(Law):
    definition: Callable[[Law1, _TypeArgType1], _ReturnType]
    def __init__(self, function: Callable[[_TypeArgType1], _ReturnType]) -> None: ...

class Law2(Law):
    definition: Callable[[Law2, _TypeArgType1, _TypeArgType2], _ReturnType]
    def __init__(self, function: Callable[[_TypeArgType1, _TypeArgType2], _ReturnType]) -> None: ...

class Law3(Law):
    definition: Callable[[Law3, _TypeArgType1, _TypeArgType2, _TypeArgType3], _ReturnType]
    def __init__(self, function: Callable[[_TypeArgType1, _TypeArgType2, _TypeArgType3], _ReturnType]) -> None: ...

class Lawful:
    @classmethod
    def laws(cls: Any) -> Dict[Type[Lawful], Sequence[Law]]: ...

class LawSpecDef: ...
