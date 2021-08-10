from __future__ import absolute_import
from returns.context import RequiresContext


def test_context_ask():
    u"""Ensures that ``ask`` method works correctly."""
    assert RequiresContext[unicode, int].ask()(1) == 1
    assert RequiresContext[int, unicode].ask()(u'a') == u'a'


def test_requires_context_from_value():
    u"""Ensures that ``from_value`` method works correctly."""
    assert RequiresContext.from_value(1)(RequiresContext.no_args) == 1
    assert RequiresContext.from_value(2)(1) == 2
