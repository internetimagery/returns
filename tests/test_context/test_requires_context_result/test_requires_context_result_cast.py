from __future__ import division
from __future__ import absolute_import
from returns.context import (
    ReaderResult,
    ReaderResultE,
    RequiresContextResult,
    RequiresContextResultE,
)


def _function(arg):
    if arg == 0:
        return RequiresContextResult.from_failure(
            ZeroDivisionError(u'Divided by 0'),
        )
    return RequiresContextResult.from_value(10 / arg)


def test_requires_context_resulte():
    u"""Ensures that RequiresContextResultE correctly typecast."""
    container: RequiresContextResult[float, Exception, int] = _function(1)
    assert container(0) == RequiresContextResult.from_value(10.0)(0)


def test_requires_context_aliases():
    u"""Ensures that ReaderResult correctly typecast."""
    container: ReaderResultE[float, int] = _function(1)
    container2: ReaderResult[float, Exception, int] = _function(1)
    container3: ReaderResultE[float, int] = ReaderResultE.from_value(
        10.0,
    )
    container4: ReaderResultE[float, int] = ReaderResult.from_value(10.0)

    assert container(0) == container2(0) == container3(0) == container4(0)
    assert container(0) == RequiresContextResult.from_value(10.0)(0)
