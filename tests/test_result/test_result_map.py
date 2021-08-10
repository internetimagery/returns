from __future__ import absolute_import
from returns.result import Failure, Success


def test_map_success():
    u"""Ensures that Success is mappable."""
    assert Success(5).map(unicode) == Success(u'5')


def test_alt_failure():
    u"""Ensures that Failure is mappable."""
    assert Failure(5).map(unicode) == Failure(5)
    assert Failure(5).alt(unicode) == Failure(u'5')


def test_alt_success():
    u"""Ensures that Success.alt is NoOp."""
    assert Success(5).alt(unicode) == Success(5)
