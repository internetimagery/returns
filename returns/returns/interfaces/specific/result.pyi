import abc
from abc import abstractmethod
from returns.interfaces import equable as equable, failable as failable, unwrappable as unwrappable
from returns.primitives.hkt import KindN as KindN
from returns.result import Result as Result
from typing import Any, Callable, Type

class ResultLikeN(failable.DiverseFailableN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta):
    @abstractmethod
    def bind_result(self, function: Callable[[_FirstType], Result[_UpdatedType, _SecondType]]) -> KindN[_ResultLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @classmethod
    @abstractmethod
    def from_result(cls: Type[_ResultLikeType], inner_value: Result[_ValueType, _ErrorType]) -> KindN[_ResultLikeType, _ValueType, _ErrorType, _ThirdType]: ...

ResultLike2: Any
ResultLike3: Any

class UnwrappableResult(ResultLikeN[_FirstType, _SecondType, _ThirdType], unwrappable.Unwrappable[_FirstUnwrappableType, _SecondUnwrappableType], equable.Equable, metaclass=abc.ABCMeta): ...
class ResultBasedN(UnwrappableResult[_FirstType, _SecondType, _ThirdType, _FirstType, _SecondType], metaclass=abc.ABCMeta): ...

ResultBased2: Any
ResultBased3: Any
