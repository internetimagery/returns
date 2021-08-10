from __future__ import absolute_import
from typing import TYPE_CHECKING, Awaitable, Callable, TypeVar

from returns.primitives.hkt import Kind3, dekind
from returns.result import Result

if TYPE_CHECKING:
    from returns.context import RequiresContextFutureResult  # noqa: F401

_ValueType = TypeVar(u'_ValueType', covariant=True)
_NewValueType = TypeVar(u'_NewValueType')
_ErrorType = TypeVar(u'_ErrorType', covariant=True)
_EnvType = TypeVar(u'_EnvType')


async def async_bind_async(
    function,
    container,
    deps,
):
    u"""Async binds a coroutine with container over a value."""
    inner_value = await container(deps)._inner_value
    if isinstance(inner_value, Result.success_type):
        return await dekind(
            await function(inner_value.unwrap()),
        )(deps)._inner_value
    return inner_value  # type: ignore[return-value]


async def async_compose_result(
    function,
    container,
    deps,
):
    u"""Async composes ``Result`` based function."""
    new_container = dekind(function((await container(deps))._inner_value))
    return (await new_container(deps))._inner_value
