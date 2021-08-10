from __future__ import with_statement
from __future__ import absolute_import
from typing import Type

import pytest

from returns.functions import raise_exception
from returns.result import Failure, Success


class _CustomException(Exception):
    u"""Just for the test."""


@pytest.mark.parametrize(u'exception_type', [
    TypeError,
    ValueError,
    _CustomException,
])
def test_raise_regular_exception(exception_type):
    u"""Ensures that regular exception can be thrown."""
    with pytest.raises(exception_type):
        raise_exception(exception_type())


def test_failure_can_be_alted():
    u"""Ensures that exceptions can work with Failures."""
    failure = Failure(ValueError(u'Message'))
    with pytest.raises(ValueError, match=u'Message'):
        failure.alt(raise_exception)


def test_success_is_not_touched():
    u"""Ensures that exceptions can work with Success."""
    assert Success(1).alt(raise_exception) == Success(1)
