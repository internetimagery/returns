from __future__ import absolute_import
from typing import List, Tuple

import pytest

from returns.future import FutureResult
from returns.io import IOFailure, IOSuccess
from returns.pipeline import managed
from returns.result import Failure, Result, Success


def _acquire_success():
    return FutureResult.from_value(u'acquire success')


def _acquire_failure():
    return FutureResult.from_failure(u'acquire failure')


def _use_success(inner_value):
    return FutureResult.from_value(u'use success')


def _use_failure(inner_value):
    return FutureResult.from_failure(u'use failure')


class _ReleaseSuccess(object):
    def __init__(self, logs):
        self._logs = logs

    def __call__(
        self,
        inner_value,
        use_result,
    ):
        self._logs.append((inner_value, use_result))
        return FutureResult.from_value(None)


class _ReleaseFailure(object):
    def __init__(self, logs):
        self._logs = logs

    def __call__(
        self,
        inner_value,
        use_result,
    ):
        return FutureResult.from_failure(u'release failure')


@pytest.mark.anyio()
@pytest.mark.parametrize((u'acquire', u'use', u'release', u'final_result', u'log'), [
    # Acquire success:
    (
        _acquire_success,
        _use_success,
        _ReleaseSuccess,
        IOSuccess(u'use success'),
        [(u'acquire success', Success(u'use success'))],
    ),
    (
        _acquire_success,
        _use_success,
        _ReleaseFailure,
        IOFailure(u'release failure'),
        [],
    ),
    (
        _acquire_success,
        _use_failure,
        _ReleaseSuccess,
        IOFailure(u'use failure'),
        [(u'acquire success', Failure(u'use failure'))],
    ),
    (
        _acquire_success,
        _use_failure,
        _ReleaseFailure,
        IOFailure(u'release failure'),
        [],
    ),

    # Acquire failure:
    (
        _acquire_failure,
        _use_success,
        _ReleaseSuccess,
        IOFailure(u'acquire failure'),
        [],
    ),
    (
        _acquire_failure,
        _use_failure,
        _ReleaseSuccess,
        IOFailure(u'acquire failure'),
        [],
    ),
    (
        _acquire_failure,
        _use_success,
        _ReleaseFailure,
        IOFailure(u'acquire failure'),
        [],
    ),
    (
        _acquire_failure,
        _use_failure,
        _ReleaseFailure,
        IOFailure(u'acquire failure'),
        [],
    ),
])
async def test_all_success(acquire, use, release, final_result, log):
    u"""Ensures that managed works as intended."""
    pipeline_logs: List[Tuple[unicode, Result[unicode, unicode]]] = []
    pipeline_result = managed(
        use,
        release(pipeline_logs),
    )(acquire())

    assert await pipeline_result == final_result
    assert pipeline_logs == log


@pytest.mark.anyio()
async def test_full_typing():
    u"""This test is here to be a case for typing."""
    logs: List[Tuple[unicode, Result[unicode, unicode]]] = []
    pipeline_result = managed(
        _use_success,
        _ReleaseSuccess(logs),
    )(_acquire_success())

    assert await pipeline_result == IOSuccess(u'use success')
    assert logs == [(u'acquire success', Success(u'use success'))]
