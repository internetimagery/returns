from __future__ import division
from __future__ import absolute_import
from typing import Callable

from returns.context import RequiresContext


def _same_function(some_arg):
    return lambda other: other / some_arg


def test_equality():
    u"""Ensures that containers can be compared."""
    assert RequiresContext(_same_function) == RequiresContext(_same_function)


def test_nonequality():
    u"""Ensures that containers can be compared."""
    assert RequiresContext(_same_function) != RequiresContext(unicode)
    assert RequiresContext.from_value(1) != RequiresContext.from_value(1)
