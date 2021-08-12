from functools import wraps
from typing import Any, Callable, Tuple, Type, TypeVar, Union, overload

from returns.result import Result, Success, Failure


_ValueType = TypeVar("_ValueType")
_ErrorType = TypeVar("_ErrorType")

_Callee = Callable[..., _ValueType]
_Caller = Callable[..., Result[_ValueType, _ErrorType]]

# Placeholder Errors
E1 = TypeVar("E1", bound=BaseException)
E2 = TypeVar("E2", bound=BaseException)
E3 = TypeVar("E3", bound=BaseException)
E4 = TypeVar("E4", bound=BaseException)
E5 = TypeVar("E5", bound=BaseException)


@overload
def catch(
    error: Type[E1],
    function: _Callee[_ValueType],
) -> _Caller[_ValueType, E1]:
    ...


@overload
def catch(
    error: Tuple[Type[E1]],
    function: _Callee[_ValueType],
) -> _Caller[_ValueType, E1]:
    ...


@overload
def catch(
    error: Tuple[Type[E1], Type[E2]],
    function: _Callee[_ValueType],
) -> _Caller[_ValueType, Union[E1, E2]]:
    ...


@overload
def catch(
    error: Tuple[Type[E1], Type[E2], Type[E3]],
    function: _Callee[_ValueType],
) -> _Caller[_ValueType, Union[E1, E2, E3]]:
    ...


@overload
def catch(
    error: Tuple[Type[E1], Type[E2], Type[E3], Type[E4]],
    function: _Callee[_ValueType],
) -> _Caller[_ValueType, Union[E1, E2, E3, E4]]:
    ...


@overload
def catch(
    error: Tuple[Type[E1], Type[E2], Type[E3], Type[E4], Type[E5]],
    function: _Callee[_ValueType],
) -> _Caller[_ValueType, Union[E1, E2, E3, E4, E5]]:
    ...


@overload
def catch(
    error: Tuple[Type[E1], ...],
    function: _Callee[_ValueType],
) -> _Caller[_ValueType, E1]:
    ...


def catch(error: Any, function: Callable) -> Callable:
    @wraps(function)
    def decorator(*args, **kwargs) -> Result:
        try:
            return Success(function(*args, **kwargs))
        except error as exc:
            return Failure(exc)
    return decorator
