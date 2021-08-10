from __future__ import with_statement
from __future__ import absolute_import
import pytest

from returns.primitives.exceptions import UnwrapFailedError
from returns.result import Failure, Success


def test_unwrap_success():
    u"""Ensures that unwrap works for Success container."""
    assert Success(5).unwrap() == 5


def test_unwrap_failure():
    u"""Ensures that unwrap works for Failure container."""
    with pytest.raises(UnwrapFailedError):
        assert Failure(5).unwrap()


def test_unwrap_failure_with_exception():
    u"""Ensures that unwrap raises from the original exception."""
    expected_exception = ValueError(u'error')
    with pytest.raises(UnwrapFailedError) as excinfo:
        Failure(expected_exception).unwrap()

    assert u'ValueError: error' in unicode(
        excinfo.getrepr(),  # noqa: WPS441
    )
