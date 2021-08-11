from __future__ import absolute_import
from typing import TYPE_CHECKING, Awaitable, Callable, TypeVar

from trollius import coroutine, From, Return

from returns.primitives.hkt import Kind3, dekind
from returns.result import Result

if TYPE_CHECKING:
    from returns.context import RequiresContextFutureResult  # noqa: F401

_ValueType = TypeVar(u'_ValueType', covariant=True)
_NewValueType = TypeVar(u'_NewValueType')
_ErrorType = TypeVar(u'_ErrorType', covariant=True)
_EnvType = TypeVar(u'_EnvType')


@coroutine
def async_bind_async(
    function,
    container,
    deps,
):
    u"""Async binds a coroutine with container over a value."""
    inner_value = yield From( container(deps) )._inner_value
    if isinstance(inner_value, Result.success_type):
        raise Return( yield From( dekind(
            (yield From( function(inner_value.unwrap()) )),
        ) )(deps)._inner_value )
    raise Return( inner_value )  # type: ignore[return-value]


@coroutine
def async_compose_result(
    function,
    container,
    deps,
):
    u"""Async composes ``Result`` based function."""
    new_container = dekind(function(((yield From( container(deps) )))._inner_value))
    raise Return( ((yield From( new_container(deps) )))._inner_value )
