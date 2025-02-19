from __future__ import with_statement
from __future__ import absolute_import
from copy import copy, deepcopy

import pytest

from returns.context import RequiresContextIOResult
from returns.primitives.exceptions import ImmutableStateError


def test_requires_context_result_immutable():
    u"""Ensures that container is immutable."""
    with pytest.raises(ImmutableStateError):
        RequiresContextIOResult.from_value(1).abc = 1


def test_requires_context_result_immutable_copy():
    u"""Ensures that helper returns it self when passed to copy function."""
    context_ioresult = RequiresContextIOResult.from_value(1)
    assert context_ioresult is copy(context_ioresult)


def test_requires_context_result_immutable_deepcopy():  # noqa: WPS118
    u"""Ensures that helper returns it self when passed to deepcopy function."""
    requires_context = RequiresContextIOResult.from_value(1)
    assert requires_context is deepcopy(requires_context)
