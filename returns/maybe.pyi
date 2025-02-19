from abc import ABCMeta
from returns.interfaces.specific.maybe import MaybeBased2 as MaybeBased2
from returns.primitives.container import BaseContainer as BaseContainer
from returns.primitives.hkt import Kind1 as Kind1, SupportsKind1 as SupportsKind1
from typing import Any, Callable, ClassVar, NoReturn, Optional, Type, Union

class Maybe(BaseContainer, SupportsKind1['Maybe', _ValueType], MaybeBased2[_ValueType, None], metaclass=ABCMeta):
    __match_args__: Any = ...
    empty: ClassVar[Maybe[Any]]
    success_type: ClassVar[Type[Some]]
    failure_type: ClassVar[Type[_Nothing]]
    equals: Any = ...
    def map(self, function: Callable[[_ValueType], _NewValueType]) -> Maybe[_NewValueType]: ...
    def apply(self, function: Kind1[Maybe, Callable[[_ValueType], _NewValueType]]) -> Maybe[_NewValueType]: ...
    def bind(self, function: Callable[[_ValueType], Kind1[Maybe, _NewValueType]]) -> Maybe[_NewValueType]: ...
    def bind_optional(self, function: Callable[[_ValueType], Optional[_NewValueType]]) -> Maybe[_NewValueType]: ...
    def lash(self, function: Callable[[Any], Kind1[Maybe, _ValueType]]) -> Maybe[_ValueType]: ...
    def value_or(self, default_value: _NewValueType) -> Union[_ValueType, _NewValueType]: ...
    def or_else_call(self, function: Callable[[], _NewValueType]) -> Union[_ValueType, _NewValueType]: ...
    def unwrap(self) -> _ValueType: ...
    def failure(self) -> None: ...
    @classmethod
    def from_value(cls: Any, inner_value: _NewValueType) -> Maybe[_NewValueType]: ...
    @classmethod
    def from_optional(cls: Any, inner_value: Optional[_NewValueType]) -> Maybe[_NewValueType]: ...

class _Nothing(Maybe[Any]):
    def __new__(cls: Any, *args: Any, **kwargs: Any) -> _Nothing: ...
    def __init__(self, inner_value: None=...) -> None: ...
    def map(self, function: Any) -> Any: ...
    def apply(self, container: Any) -> Any: ...
    def bind(self, function: Any) -> Any: ...
    def bind_optional(self, function: Any) -> Any: ...
    def lash(self, function: Any) -> Any: ...
    def value_or(self, default_value: Any) -> Any: ...
    def or_else_call(self, function: Any) -> Any: ...
    def unwrap(self) -> None: ...
    def failure(self) -> None: ...

class Some(Maybe[_ValueType]):
    def __init__(self, inner_value: _ValueType) -> None: ...
    def map(self, function: Any) -> Any: ...
    def apply(self, container: Any) -> Any: ...
    def lash(self, function: Any) -> Any: ...
    def value_or(self, default_value: Any) -> Any: ...
    def or_else_call(self, function: Any) -> Any: ...
    def failure(self) -> None: ...

Nothing: Maybe[NoReturn]

def maybe(function: Callable[..., Optional[_ValueType]]) -> Callable[..., Maybe[_ValueType]]: ...
