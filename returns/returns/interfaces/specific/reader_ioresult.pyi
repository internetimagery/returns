import abc
from abc import abstractmethod
from returns.context import ReaderIOResult as ReaderIOResult
from returns.interfaces.specific import ioresult as ioresult, reader as reader, reader_result as reader_result
from returns.primitives.hkt import KindN as KindN
from returns.primitives.laws import LawSpecDef as LawSpecDef, Lawful as Lawful
from typing import Any, Callable, Type

class ReaderIOResultLikeN(reader_result.ReaderResultLikeN[_FirstType, _SecondType, _ThirdType], ioresult.IOResultLikeN[_FirstType, _SecondType, _ThirdType], metaclass=abc.ABCMeta):
    @abstractmethod
    def bind_context_ioresult(self, function: Callable[[_FirstType], ReaderIOResult[_UpdatedType, _SecondType, _ThirdType]]) -> KindN[_ReaderIOResultLikeType, _UpdatedType, _SecondType, _ThirdType]: ...
    @classmethod
    @abstractmethod
    def from_ioresult_context(cls: Type[_ReaderIOResultLikeType], inner_value: ReaderIOResult[_ValueType, _ErrorType, _EnvType]) -> KindN[_ReaderIOResultLikeType, _ValueType, _ErrorType, _EnvType]: ...

ReaderIOResultLike3: Any

class _LawSpec(LawSpecDef):
    def asking_law(container: ReaderIOResultBasedN[_FirstType, _SecondType, _ThirdType], env: _ThirdType) -> None: ...

class ReaderIOResultBasedN(ReaderIOResultLikeN[_FirstType, _SecondType, _ThirdType], reader.CallableReader3[_FirstType, _SecondType, _ThirdType, 'IOResult[_FirstType, _SecondType]', _ThirdType], Lawful['ReaderIOResultBasedN[_FirstType, _SecondType, _ThirdType]'], metaclass=abc.ABCMeta): ...

ReaderIOResultBased3: Any
