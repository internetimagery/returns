from __future__ import absolute_import
from typing import Any, Sequence, Type

import pytest
from hypothesis import given
from hypothesis import strategies as st

from returns.context import (
    Reader,
    RequiresContext,
    RequiresContextFutureResult,
    RequiresContextIOResult,
    RequiresContextResult,
    RequiresContextResultE,
)
from returns.future import Future, FutureResult
from returns.io import IO, IOResult
from returns.maybe import Maybe
from returns.pipeline import is_successful
from returns.primitives.laws import Lawful
from returns.result import Result, ResultE

_all_containers: Sequence[Type[Lawful]] = (
    Maybe,
    Result,
    IO,
    IOResult,
    Future,
    FutureResult,
    RequiresContext,
    RequiresContextResult,
    RequiresContextIOResult,
    RequiresContextFutureResult,

    # Aliases:
    ResultE,
    Reader,
    RequiresContextResultE,
)


@pytest.mark.filterwarnings(u'ignore:.*')
@pytest.mark.parametrize(u'container_type', _all_containers)
def test_all_containers_resolves(container_type):
    u"""Ensures all containers do resolve."""
    assert st.from_type(container_type).example()


@given(
    st.from_type(ResultE).filter(
        lambda container: not is_successful(container),
    ),
)
def test_result_error_alias_resolves(thing):
    u"""Ensures that type aliases are resolved correctly."""
    assert isinstance(thing.failure(), Exception)


CustomResult = Result[int, unicode]


@given(st.from_type(CustomResult))
def test_custom_result_error_types_resolve(thing):
    u"""Ensures that type aliases are resolved correctly."""
    if is_successful(thing):
        assert isinstance(thing.unwrap(), int)
    else:
        assert isinstance(thing.failure(), unicode)


@given(
    st.from_type(RequiresContextResultE).filter(
        lambda container: not is_successful(
            container(RequiresContextResultE.no_args),
        ),
    ),
)
def test_reader_result_error_alias_resolves(
    thing,
):
    u"""Ensures that type aliases are resolved correctly."""
    real_result = thing(RequiresContextResultE.no_args)
    assert isinstance(real_result.failure(), Exception)


CustomReaderResult = RequiresContextResult[int, unicode, bool]


@given(st.from_type(CustomReaderResult))
def test_custom_readerresult_types_resolve(
    thing,
):
    u"""Ensures that type aliases are resolved correctly."""
    real_result = thing(RequiresContextResultE.no_args)
    if is_successful(real_result):
        assert isinstance(real_result.unwrap(), int)
    else:
        assert isinstance(real_result.failure(), unicode)
