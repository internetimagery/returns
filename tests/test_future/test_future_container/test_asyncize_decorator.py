from __future__ import division
from __future__ import absolute_import
import pytest

from returns.future import asyncify


@asyncify
def _function(arg):
    return arg / 2


@pytest.mark.anyio()
async def test_asyncify_decorator():
    u"""Ensure that function marked with ``@asyncify`` is awaitable."""
    coro = _function(2)

    assert await coro == 1
