
from __future__ import division
from __future__ import absolute_import
from returns.result import Success, safe


@safe
def _function(number):
    return number / number


def test_safe_success():
    u"""Ensures that safe decorator works correctly for Success case."""
    assert _function(1) == Success(1.0)


def test_safe_failure():
    u"""Ensures that safe decorator works correctly for Failure case."""
    failed = _function(0)
    assert isinstance(failed.failure(), ZeroDivisionError)
