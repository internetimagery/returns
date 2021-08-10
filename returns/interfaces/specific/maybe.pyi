import abc
from abc import abstractmethod
from returns.interfaces import equable as equable, failable as failable, unwrappable as unwrappable
from returns.primitives.hkt import KindN as KindN
from returns.primitives.laws import LawSpecDef as LawSpecDef, Lawful as Lawful
from typing import Any, Callable, Optional, Type, Union

class _LawSpec(LawSpecDef):
    def map_short_circuit_law(container: MaybeLikeN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], _NewType1]) -> None: ...
    def bind_short_circuit_law(container: MaybeLikeN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], KindN[MaybeLikeN, _NewType1, _SecondType, _ThirdType]]) -> None: ...
    def bind_optional_short_circuit_law(container: MaybeLikeN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], Optional[_NewType1]]) -> None: ...
    def lash_short_circuit_law(raw_value: _FirstType, container: MaybeLikeN[_FirstType, _SecondType, _ThirdType], function: Callable[[_SecondType], KindN[MaybeLikeN, _FirstType, _NewType1, _ThirdType]]) -> None: ...
    def unit_structure_law(container: MaybeLikeN[_FirstType, _SecondType, _ThirdType], function: Callable[[_FirstType], None]) -> None: ...

class MaybeLikeN(failable.SingleFailableN[_FirstType, _SecondType, _ThirdType], Lawful['MaybeLikeN[_FirstType, _SecondType, _ThirdType]'], metaclass=abc.ABCMeta):
    @abstractmethod
    def bind_optional(self, function: Callable[[_FirstType], Optional[_UpdatedType]]) -> KindN[_MaybeLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @classmethod
    @abstractmethod
    def from_optional(cls: Type[_MaybeLikeType], inner_value: Optional[_ValueType]) -> KindN[_MaybeLikeType, _ValueType, _SecondType, _ThirdType]: ...

MaybeLike2: Any
MaybeLike3: Any

class MaybeBasedN(MaybeLikeN[_FirstType, _SecondType, _ThirdType], unwrappable.Unwrappable[_FirstType, None], equable.Equable, metaclass=abc.ABCMeta):
    @abstractmethod
    def or_else_call(self, function: Callable[[], _ValueType]) -> Union[_FirstType, _ValueType]: ...

MaybeBased2: Any
MaybeBased3: Any
