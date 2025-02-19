from __future__ import absolute_import
from returns.io import IO


def test_io_pickle():
    u"""Tests how pickle protocol works for containers."""
    assert IO(1).__getstate__() == 1  # noqa: WPS609


def test_io_pickle_restore():
    u"""Ensures that object can be restored."""
    container = IO(2)
    container.__setstate__(1)  # noqa: WPS609
    assert container == IO(1)
