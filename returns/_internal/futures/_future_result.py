from __future__ import absolute_import
from typing import TYPE_CHECKING, Any, Callable, TypeVar

from trollius import coroutine, From, Return

from returns.io import IO, IOResult
from returns.primitives.hkt import Kind2, dekind
from returns.result import Failure, Result, Success

if TYPE_CHECKING:
    from typing import Awaitable
    from returns.future import Future, FutureResult  # noqa: F401


_ValueType = TypeVar(u'_ValueType', covariant=True)
_NewValueType = TypeVar(u'_NewValueType')
_ErrorType = TypeVar(u'_ErrorType', covariant=True)
_NewErrorType = TypeVar(u'_NewErrorType')


@coroutine
def async_swap(
    inner_value,
):
    u"""Swaps value and error types in ``Result``."""
    raise Return( ((yield From( inner_value ))).swap() )


@coroutine
def async_map(
    function,
    inner_value,
):
    u"""Async maps a function over a value."""
    raise Return( ((yield From( inner_value ))).map(function) )


@coroutine
def async_apply(
    container,
    inner_value,
):
    u"""Async maps a function over a value."""
    raise Return( ((yield From( inner_value ))).apply(((yield From( container )))._inner_value) )


@coroutine
def async_bind(
    function,
    inner_value,
):
    u"""Async binds a container over a value."""
    container = (yield From( inner_value ))
    if isinstance(container, Result.success_type):
        raise Return( ((yield From( dekind(function(container.unwrap())) )))._inner_value )
    raise Return( container )  # type: ignore[return-value]


@coroutine
def async_bind_awaitable(
    function,
    inner_value,
):
    u"""Async binds a coroutine over a value."""
    container = (yield From( inner_value ))
    if isinstance(container, Result.success_type):
        raise Return( Result.from_value((yield From( function(container.unwrap()) ))) )
    raise Return( container )  # type: ignore[return-value]


@coroutine
def async_bind_async(
    function,
    inner_value,
):
    u"""Async binds a coroutine with container over a value."""
    container = (yield From( inner_value ))
    if isinstance(container, Result.success_type):
        raise Return( (yield From( dekind((yield From( function(container.unwrap()) ))) ))._inner_value )
    raise Return( container )  # type: ignore[return-value]


@coroutine
def async_bind_result(
    function,
    inner_value,
):
    u"""Async binds a container returning ``Result`` over a value."""
    raise Return( ((yield From( inner_value ))).bind(function) )


@coroutine
def async_bind_ioresult(
    function,
    inner_value,
):
    u"""Async binds a container returning ``IOResult`` over a value."""
    container = (yield From( inner_value ))
    if isinstance(container, Result.success_type):
        raise Return( function(container.unwrap())._inner_value )
    raise Return( container )  # type: ignore[return-value]


@coroutine
def async_bind_io(
    function,
    inner_value,
):
    u"""Async binds a container returning ``IO`` over a value."""
    container = (yield From( inner_value ))
    if isinstance(container, Result.success_type):
        raise Return( Success(function(container.unwrap())._inner_value) )
    raise Return( container )  # type: ignore[return-value]


@coroutine
def async_bind_future(
    function,
    inner_value,
):
    u"""Async binds a container returning ``IO`` over a value."""
    container = (yield From( inner_value ))
    if isinstance(container, Result.success_type):
        raise Return( (yield From( async_from_success(function(container.unwrap())) )) )
    raise Return( container )  # type: ignore[return-value]


@coroutine
def async_bind_async_future(
    function,
    inner_value,
):
    u"""Async binds a container returning ``IO`` over a value."""
    container = (yield From( inner_value ))
    if isinstance(container, Result.success_type):
        raise Return( (yield From( async_from_success((yield From( function(container.unwrap()) ))) )) )
    raise Return( container )  # type: ignore[return-value]


@coroutine
def async_alt(
    function,
    inner_value,
):
    u"""Async alts a function over a value."""
    container = (yield From( inner_value ))
    if isinstance(container, Result.success_type):
        raise Return( container )
    raise Return( Failure(function(container.failure())) )


@coroutine
def async_lash(
    function,
    inner_value,
):
    u"""Async lashes a function returning a container over a value."""
    container = (yield From( inner_value ))
    if isinstance(container, Result.success_type):
        raise Return( container )
    raise Return( ((yield From( dekind(function(container.failure())) )))._inner_value )


@coroutine
def async_from_success(
    container,
):
    u"""Async success unit factory."""
    raise Return( Success(((yield From( container )))._inner_value) )


@coroutine
def async_from_failure(
    container,
):
    u"""Async failure unit factory."""
    raise Return( Failure(((yield From( container )))._inner_value) )


@coroutine
def async_compose_result(
    function,
    inner_value,
):
    u"""Async composes ``Result`` based function."""
    raise Return( ((yield From( dekind(function((yield From( inner_value )))) )))._inner_value )
