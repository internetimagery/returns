from __future__ import division
from __future__ import absolute_import
from returns.context import (
    ReaderIOResult,
    ReaderIOResultE,
    RequiresContextIOResult,
    RequiresContextIOResultE,
)


def _function(arg):
    if arg == 0:
        return RequiresContextIOResult.from_failure(
            ZeroDivisionError(u'Divided by 0'),
        )
    return RequiresContextIOResult.from_value(10 / arg)


def test_requires_context_ioresulte():
    u"""Ensures that RequiresContextIOResultE correctly typecast."""
    container: RequiresContextIOResult[float, Exception, int] = _function(1)
    assert container(0) == RequiresContextIOResult.from_value(10.0)(0)


def test_requires_context_io_aliases():
    u"""Ensures that ReaderIOResult correctly typecast."""
    container: ReaderIOResultE[float, int] = _function(1)
    container2: ReaderIOResult[float, Exception, int] = _function(1)
    container3: ReaderIOResultE[float, int] = ReaderIOResultE.from_value(
        10.0,
    )
    container4: ReaderIOResultE[float, int] = ReaderIOResult.from_value(10.0)

    assert container(0) == container2(0) == container3(0) == container4(0)
    assert container(0) == RequiresContextIOResult.from_value(10.0)(0)
