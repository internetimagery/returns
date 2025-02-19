from __future__ import with_statement
from __future__ import absolute_import
from copy import copy, deepcopy

import pytest

from returns.context import RequiresContextResult
from returns.primitives.exceptions import ImmutableStateError


def test_immutable_copy():
    u"""Ensures that helper returns it self when passed to copy function."""
    context_result = RequiresContextResult.from_value(1)
    assert context_result is copy(context_result)


def test_immutable_deepcopy():
    u"""Ensures that helper returns it self when passed to deepcopy function."""
    context_result = RequiresContextResult.from_value(1)
    assert context_result is deepcopy(context_result)


def test_requires_context_result_immutable():
    u"""Ensures that container is immutable."""
    with pytest.raises(ImmutableStateError):
        RequiresContextResult.from_value(1).abc = 1
