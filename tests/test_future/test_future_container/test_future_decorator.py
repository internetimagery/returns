from __future__ import division
from __future__ import absolute_import
import pytest

from returns.future import Future, future
from returns.io import IO


@future
async def _coro(arg):
    return arg / 2


@pytest.mark.anyio()
async def test_safe_decorator():
    u"""Ensure that coroutine marked with ``@future`` returns ``Future``."""
    future_instance = _coro(1)

    assert isinstance(future_instance, Future)
    assert await future_instance == IO(0.5)
