from __future__ import absolute_import
from returns.result import Failure, Result, Success


def test_bind():
    u"""Ensures that bind works."""
    def factory(inner_value):
        if inner_value > 0:
            return Success(inner_value * 2)
        return Failure(unicode(inner_value))

    input_value = 5
    bound: Result[int, unicode] = Success(input_value)

    assert bound.bind(factory) == factory(input_value)
    assert Success(input_value).bind(factory) == factory(input_value)
    assert unicode(bound.bind(factory)) == u'<Success: 10>'

    input_value = 0
    bound2: Result[int, unicode] = Success(input_value)

    assert bound2.bind(factory) == factory(input_value)
    assert unicode(bound2.bind(factory)) == u'<Failure: 0>'


def test_left_identity_success():
    u"""Ensures that left identity works for Success container."""
    def factory(inner_value):
        return Success(inner_value * 2)

    input_value = 5
    bound: Result[int, unicode] = Success(input_value)

    assert bound.bind(factory) == factory(input_value)


def test_left_identity_failure():
    u"""Ensures that left identity works for Failure container."""
    def factory(inner_value):
        return Failure(6)

    input_value = 5
    bound: Result[int, int] = Failure(input_value)

    assert bound.bind(factory) == Failure(input_value)
    assert Failure(input_value).bind(factory) == Failure(5)
    assert unicode(bound) == u'<Failure: 5>'


def test_lash_success():
    u"""Ensures that lash works for Success container."""
    def factory(inner_value):
        return Success(inner_value * 2)

    bound = Success(5).lash(factory)

    assert bound == Success(5)
    assert Success(5).lash(factory) == Success(5)
    assert unicode(bound) == u'<Success: 5>'


def test_lash_failure():
    u"""Ensures that lash works for Failure container."""
    def factory(inner_value):
        return Failure(inner_value + 1)

    expected = 6
    bound: Result[unicode, int] = Failure(5)

    assert bound.lash(factory) == Failure(expected)
    assert Failure(5).lash(factory) == Failure(expected)
    assert unicode(bound.lash(factory)) == u'<Failure: 6>'
