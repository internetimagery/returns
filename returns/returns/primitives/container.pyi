from abc import ABCMeta
from returns.primitives.hkt import Kind1 as Kind1
from returns.primitives.types import Immutable as Immutable
from typing import Any

class BaseContainer(Immutable, metaclass=ABCMeta):
    def __init__(self, inner_value: Any) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

def container_equality(self, other: Kind1[_EqualType, Any]) -> bool: ...
