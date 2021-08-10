from __future__ import absolute_import
from typing import Optional

from returns.maybe import Maybe, Nothing, Some


def test_bind_some():
    u"""Ensures that bind works correctly."""
    def factory(inner_value):
        return Some(inner_value * 2)

    input_value = 5
    bound = Some(input_value).bind(factory)

    assert bound == factory(input_value)
    assert unicode(bound) == u'<Some: 10>'


def test_bind_optional():
    u"""Ensures that bind_optional works correctly."""
    def factory(inner_value):
        return inner_value if inner_value else None

    assert Some(1).bind_optional(factory) == Some(1)
    assert Some(0).bind_optional(factory) == Nothing
    assert Nothing.bind_optional(factory) == Nothing
