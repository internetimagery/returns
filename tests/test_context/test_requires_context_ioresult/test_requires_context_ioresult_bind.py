from __future__ import division
from __future__ import absolute_import
from returns.context import RequiresContext
from returns.context import RequiresContextIOResult as RCR  # noqa: N814
from returns.context import RequiresContextResult
from returns.io import IOFailure, IOResult, IOSuccess
from returns.result import Failure, Result, Success


def test_bind():
    u"""Ensures that bind works."""
    def factory(inner_value):
        if inner_value > 0:
            return RCR(lambda deps: IOSuccess(inner_value / deps))
        return RCR.from_failure(unicode(inner_value))

    input_value = 5
    bound: RCR[int, unicode, int] = RCR.from_value(input_value)
    assert bound.bind(factory)(2) == factory(input_value)(2)
    assert bound.bind(factory)(2) == IOSuccess(2.5)

    assert RCR.from_value(0).bind(
        factory,
    )(2) == factory(0)(2) == IOFailure(u'0')


def test_bind_regular_result():
    u"""Ensures that regular ``Result`` can be bound."""
    def factory(inner_value):
        if inner_value > 0:
            return Success(inner_value + 1)
        return Failure(u'nope')

    first: RCR[int, unicode, int] = RCR.from_value(1)
    third: RCR[int, unicode, int] = RCR.from_failure(u'a')

    assert first.bind_result(factory)(RCR.no_args) == IOSuccess(2)
    assert RCR.from_value(0).bind_result(
        factory,
    )(RCR.no_args) == IOFailure(u'nope')
    assert third.bind_result(factory)(RCR.no_args) == IOFailure(u'a')


def test_bind_ioresult():
    u"""Ensures that io ``Result`` can be bound."""
    def factory(inner_value):
        if inner_value > 0:
            return IOSuccess(inner_value + 1)
        return IOFailure(u'nope')

    first: RCR[int, unicode, int] = RCR.from_value(1)
    third: RCR[int, unicode, int] = RCR.from_failure(u'a')

    assert first.bind_ioresult(factory)(RCR.no_args) == IOSuccess(2)
    assert RCR.from_value(0).bind_ioresult(
        factory,
    )(RCR.no_args) == IOFailure(u'nope')
    assert third.bind_ioresult(factory)(RCR.no_args) == IOFailure(u'a')


def test_bind_regular_context():
    u"""Ensures that regular ``RequiresContext`` can be bound."""
    def factory(inner_value):
        return RequiresContext(lambda deps: inner_value / deps)

    first: RCR[int, unicode, int] = RCR.from_value(1)
    third: RCR[int, unicode, int] = RCR.from_failure(u'a')

    assert first.bind_context(factory)(2) == IOSuccess(0.5)
    assert RCR.from_value(2).bind_context(
        factory,
    )(1) == IOSuccess(2.0)
    assert third.bind_context(factory)(1) == IOFailure(u'a')


def test_bind_result_context():
    u"""Ensures that ``RequiresContextResult`` can be bound."""
    def factory(inner_value):
        return RequiresContextResult(lambda deps: Success(inner_value / deps))

    first: RCR[int, unicode, int] = RCR.from_value(1)
    third: RCR[int, unicode, int] = RCR.from_failure(u'a')

    assert first.bind_context_result(factory)(2) == IOSuccess(0.5)
    assert RCR.from_value(2).bind_context_result(
        factory,
    )(1) == IOSuccess(2.0)
    assert third.bind_context_result(factory)(1) == IOFailure(u'a')


def test_lash_success():
    u"""Ensures that lash works for Success container."""
    def factory(inner_value):
        return RCR.from_value(inner_value * 2)

    assert RCR.from_value(5).lash(
        factory,
    )(0) == RCR.from_value(5)(0)
    assert RCR.from_failure(5).lash(
        factory,
    )(0) == RCR.from_value(10)(0)


def test_lash_failure():
    u"""Ensures that lash works for Failure container."""
    def factory(inner_value):
        return RCR.from_failure(inner_value * 2)

    assert RCR.from_value(5).lash(
        factory,
    )(0) == RCR.from_value(5)(0)
    assert RCR.from_failure(5).lash(
        factory,
    )(0) == RCR.from_failure(10)(0)
