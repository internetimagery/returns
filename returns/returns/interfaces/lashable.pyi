import abc
from abc import abstractmethod
from returns.primitives.hkt import KindN as KindN
from typing import Any, Callable

class LashableN(metaclass=abc.ABCMeta):
    @abstractmethod
    def lash(self, function: Callable[[_SecondType], KindN[_LashableType, _FirstType, _UpdatedType, _ThirdType]]) -> KindN[_LashableType, _FirstType, _UpdatedType, _ThirdType]: ...

Lashable2: Any
Lashable3: Any
