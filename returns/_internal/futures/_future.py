from __future__ import absolute_import
from typing import TYPE_CHECKING, Callable, TypeVar

from trollius import coroutine, From, Return

from returns.io import IO
from returns.primitives.hkt import Kind1, dekind

if TYPE_CHECKING:
    from typing import Awaitable
    from returns.future import Future  # noqa: F401

_ValueType = TypeVar(u'_ValueType', covariant=True)
_NewValueType = TypeVar(u'_NewValueType')


@coroutine
def async_map(
    function,
    inner_value,
):
    u"""Async maps a function over a value."""
    raise Return( function((yield From( inner_value ))) )


@coroutine
def async_apply(
    container,
    inner_value,
):
    u"""Async applies a container with function over a value."""
    raise Return( ((yield From( container )))._inner_value((yield From( inner_value ))) )


@coroutine
def async_bind(
    function,
    inner_value,
):
    u"""Async binds a container over a value."""
    raise Return( ((yield From( dekind(function((yield From( inner_value )))) )))._inner_value )


@coroutine
def async_bind_awaitable(
    function,
    inner_value,
):
    u"""Async binds a coroutine over a value."""
    raise Return( (yield From( function((yield From( inner_value ))) )) )


@coroutine
def async_bind_async(
    function,
    inner_value,
):
    u"""Async binds a coroutine with container over a value."""
    inner_io = dekind((yield From( function((yield From( inner_value ))) )))._inner_value
    raise Return( (yield From( inner_io )) )


@coroutine
def async_bind_io(
    function,
    inner_value,
):
    u"""Async binds a container over a value."""
    raise Return( function((yield From( inner_value )))._inner_value )
