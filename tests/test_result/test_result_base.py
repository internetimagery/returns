from __future__ import absolute_import
from returns.result import Result


def test_result_types():
    u"""Ensures that Result has two types inside a class."""
    assert isinstance(Result.success_type, type)
    assert isinstance(Result.failure_type, type)
