from __future__ import absolute_import
from returns.result import Failure, Success


def test_success_value():
    u"""Ensures that value is fetch correctly from the Success."""
    bound = Success(5).value_or(None)

    assert bound == 5


def test_failure_value():
    u"""Ensures that value is fetch correctly from the Failure."""
    bound = Failure(1).value_or(default_value=None)

    assert bound is None
