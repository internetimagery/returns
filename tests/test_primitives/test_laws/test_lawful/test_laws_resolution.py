from __future__ import absolute_import
from typing import List, Type

import pytest

from returns.context import (
    RequiresContext,
    RequiresContextFutureResult,
    RequiresContextIOResult,
    RequiresContextResult,
)
from returns.future import Future, FutureResult
from returns.io import IO, IOResult
from returns.maybe import Maybe
from returns.primitives.laws import Law, Lawful
from returns.result import Result


@pytest.mark.parametrize(u'container', [
    Result,
    Maybe,
    Future,
    FutureResult,
    IO,
    IOResult,
    RequiresContext,
    RequiresContextFutureResult,
    RequiresContextIOResult,
    RequiresContextResult,
])
def test_laws_resolution(container):
    u"""Ensures all tests are unique."""
    all_laws: List[Law] = []
    for laws in container.laws().values():
        all_laws.extend(laws)
    assert len(all_laws) == len(set(all_laws))
