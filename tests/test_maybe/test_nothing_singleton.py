from __future__ import absolute_import
from returns.maybe import _Nothing


def test_nothing_singleton():
    u"""Ensures `_Nothing` is a singleton."""
    assert _Nothing() is _Nothing()
