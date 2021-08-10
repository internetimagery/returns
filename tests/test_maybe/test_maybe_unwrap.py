from __future__ import with_statement
from __future__ import absolute_import
import pytest

from returns.maybe import Nothing, Some
from returns.primitives.exceptions import UnwrapFailedError


def test_unwrap_success():
    u"""Ensures that unwrap works for Some container."""
    assert Some(5).unwrap() == 5


def test_unwrap_failure():
    u"""Ensures that unwrap works for Nothing container."""
    with pytest.raises(UnwrapFailedError):
        assert Nothing.unwrap()
