from __future__ import division
from __future__ import absolute_import
import pytest

from returns.future import FutureResult, future_safe
from returns.io import IOResult, IOSuccess


@future_safe
async def _coro(arg):
    return 1 / arg


@pytest.mark.anyio()
async def test_future_safe_decorator():
    u"""Ensure that coroutine marked with ``@future_safe``."""
    future_instance = _coro(2)

    assert isinstance(future_instance, FutureResult)
    assert await future_instance == IOSuccess(0.5)


@pytest.mark.anyio()
async def test_future_safe_decorator_failure():
    u"""Ensure that coroutine marked with ``@future_safe``."""
    future_instance = _coro(0)

    assert isinstance(future_instance, FutureResult)
    assert isinstance(await future_instance, IOResult.failure_type)
