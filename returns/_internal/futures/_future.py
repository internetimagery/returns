from __future__ import absolute_import
from typing import TYPE_CHECKING, Awaitable, Callable, TypeVar

from returns.io import IO
from returns.primitives.hkt import Kind1, dekind

if TYPE_CHECKING:
    from returns.future import Future  # noqa: F401

_ValueType = TypeVar(u'_ValueType', covariant=True)
_NewValueType = TypeVar(u'_NewValueType')


async def async_map(
    function,
    inner_value,
):
    u"""Async maps a function over a value."""
    return function(await inner_value)


async def async_apply(
    container,
    inner_value,
):
    u"""Async applies a container with function over a value."""
    return (await container)._inner_value(await inner_value)


async def async_bind(
    function,
    inner_value,
):
    u"""Async binds a container over a value."""
    return (await dekind(function(await inner_value)))._inner_value


async def async_bind_awaitable(
    function,
    inner_value,
):
    u"""Async binds a coroutine over a value."""
    return await function(await inner_value)


async def async_bind_async(
    function,
    inner_value,
):
    u"""Async binds a coroutine with container over a value."""
    inner_io = dekind(await function(await inner_value))._inner_value
    return await inner_io


async def async_bind_io(
    function,
    inner_value,
):
    u"""Async binds a container over a value."""
    return function(await inner_value)._inner_value
