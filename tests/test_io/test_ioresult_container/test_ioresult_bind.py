from __future__ import absolute_import
from returns.io import IOFailure, IOResult, IOSuccess
from returns.result import Failure, Result, Success


def test_bind():
    u"""Ensures that bind works."""
    def factory(inner_value):
        if inner_value > 0:
            return IOSuccess(inner_value * 2)
        return IOFailure(unicode(inner_value))

    input_value = 5
    bound: IOResult[int, unicode] = IOSuccess(input_value)

    assert bound.bind(factory) == factory(input_value)
    assert unicode(bound.bind(factory)) == u'<IOResult: <Success: 10>>'

    input_value = 0
    bound2: IOResult[int, unicode] = IOSuccess(input_value)

    assert bound2.bind(factory) == factory(input_value)
    assert unicode(bound2.bind(factory)) == u'<IOResult: <Failure: 0>>'


def test_left_identity_success():
    u"""Ensures that left identity works for IOSuccess container."""
    def factory(inner_value):
        return IOSuccess(inner_value * 2)

    input_value = 5
    bound: IOResult[int, unicode] = IOSuccess(input_value)

    assert bound.bind(factory) == factory(input_value)


def test_left_identity_failure():
    u"""Ensures that left identity works for IOFailure container."""
    def factory(inner_value):
        return IOFailure(6)

    input_value = 5
    bound: IOResult[int, int] = IOFailure(input_value)

    assert bound.bind(factory) == IOFailure(input_value)


def test_bind_regular_result():
    u"""Ensures that regular ``Result`` can be bound to ``IOResult``."""
    def factory(inner_value):
        if inner_value > 0:
            return Success(inner_value + 1)
        return Failure(u'nope')

    first: IOResult[int, unicode] = IOSuccess(1)
    second: IOResult[int, unicode] = IOSuccess(0)
    third: IOResult[int, unicode] = IOFailure(u'a')

    assert first.bind_result(factory) == IOSuccess(2)
    assert second.bind_result(factory) == IOFailure(u'nope')
    assert third.bind_result(factory) == IOFailure(u'a')


def test_lash_success():
    u"""Ensures that lash works for IOSuccess container."""
    def factory(inner_value):
        return IOSuccess(inner_value * 2)

    bound = IOSuccess(5).lash(factory)

    assert bound == IOSuccess(5)


def test_lash_failure():
    u"""Ensures that lash works for IOFailure container."""
    def factory(inner_value):
        return IOFailure(inner_value + 1)

    expected = 6
    bound: IOResult[unicode, int] = IOFailure(5)

    assert bound.lash(factory) == IOFailure(expected)
