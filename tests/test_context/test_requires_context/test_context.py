from __future__ import with_statement
from __future__ import absolute_import
from copy import copy, deepcopy

import pytest

from returns.context import RequiresContext
from returns.primitives.exceptions import ImmutableStateError


def test_requires_context_immutable():
    u"""Ensures that Context is immutable."""
    with pytest.raises(ImmutableStateError):
        RequiresContext.from_value(1).abc = 1


def test_requires_context_immutable_copy():
    u"""Ensures that Context returns it self when passed to copy function."""
    context = RequiresContext.from_value(1)
    assert context is copy(context)


def test_requires_context_immutable_deepcopy():
    u"""Ensures that Context returns it self when passed to deepcopy function."""
    context = RequiresContext.from_value(1)
    assert context is deepcopy(context)
