import abc
from abc import abstractmethod
from returns.context import Reader as Reader, ReaderResult as ReaderResult
from returns.interfaces.specific import reader as reader, result as result
from returns.primitives.hkt import KindN as KindN
from returns.primitives.laws import LawSpecDef as LawSpecDef, Lawful as Lawful
from typing import Any, Callable, Type

class ReaderResultLikeN(reader.ReaderLike3[_FirstType, _SecondType, _ThirdType], result.ResultLikeN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta):
    @abstractmethod
    def bind_context_result(self, function: Callable[[_FirstType], ReaderResult[_UpdatedType, _SecondType, _ThirdType]]) -> KindN[_ReaderResultLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @classmethod
    @abstractmethod
    def from_failed_context(cls: Type[_ReaderResultLikeType], inner_value: Reader[_ErrorType, _EnvType]) -> KindN[_ReaderResultLikeType, _FirstType, _ErrorType, _EnvType]: ...
    @classmethod
    @abstractmethod
    def from_result_context(cls: Type[_ReaderResultLikeType], inner_value: ReaderResult[_ValueType, _ErrorType, _EnvType]) -> KindN[_ReaderResultLikeType, _ValueType, _ErrorType, _EnvType]: ...

ReaderResultLike3: Any

class _LawSpec(LawSpecDef):
    def purity_law(container: ReaderResultBasedN[_FirstType, _SecondType, _ThirdType], env: _ThirdType) -> None: ...
    def asking_law(container: ReaderResultBasedN[_FirstType, _SecondType, _ThirdType], env: _ThirdType) -> None: ...

class ReaderResultBasedN(ReaderResultLikeN[_FirstType, _SecondType, _ThirdType], reader.CallableReader3[_FirstType, _SecondType, _ThirdType, 'Result[_FirstType, _SecondType]', _ThirdType], Lawful['ReaderResultBasedN[_FirstType, _SecondType, _ThirdType]'], metaclass=abc.ABCMeta): ...

ReaderResultBased3: Any
