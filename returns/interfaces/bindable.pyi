import abc
from abc import abstractmethod
from returns.primitives.hkt import KindN as KindN
from typing import Any, Callable

class BindableN(metaclass=abc.ABCMeta):
    @abstractmethod
    def bind(self, function: Callable[[_FirstType], KindN[_BindableType, _UpdatedType, _SecondType, _ThirdType]]) -> KindN[_BindableType, _UpdatedType, _SecondType, _ThirdType]: ...

Bindable1: Any
Bindable2: Any
Bindable3: Any
