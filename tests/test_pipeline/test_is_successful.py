from __future__ import absolute_import
import pytest

from returns.io import IOFailure, IOSuccess
from returns.maybe import Nothing, Some
from returns.pipeline import is_successful
from returns.result import Failure, Success


@pytest.mark.parametrize((u'container', u'correct_result'), [
    (Success(u'a'), True),
    (Failure(u'a'), False),

    (IOSuccess(u'a'), True),
    (IOFailure(u'a'), False),

    (Some(u'a'), True),
    (Some(None), True),
    (Nothing, False),
])
def test_is_successful(container, correct_result):
    u"""Ensures that successful state works correctly."""
    assert is_successful(container) is correct_result
