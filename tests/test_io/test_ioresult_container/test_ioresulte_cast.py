from __future__ import division
from __future__ import absolute_import
from returns.io import IOFailure, IOResult, IOResultE, IOSuccess
from returns.pipeline import is_successful


def _function(arg):
    if arg == 0:
        return IOFailure(ZeroDivisionError(u'Divided by 0'))
    return IOSuccess(10 / arg)


def test_ioresulte():
    u"""Ensures that IOResultE correctly typecast."""
    container: IOResult[float, Exception] = _function(1)
    assert container == IOSuccess(10.0)

    container = _function(0)
    assert is_successful(container) is False
