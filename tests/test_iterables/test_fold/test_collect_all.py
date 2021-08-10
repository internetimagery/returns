from __future__ import with_statement
from __future__ import absolute_import
import sys
from typing import Iterable, List, Sequence, Tuple

import pytest

from returns.context import (
    NoDeps,
    ReaderFutureResult,
    ReaderIOResult,
    ReaderResult,
)
from returns.future import FutureFailure, FutureResult, FutureSuccess
from returns.io import IOFailure, IOSuccess
from returns.iterables import Fold
from returns.maybe import Nothing, Some
from returns.result import Failure, Success


@pytest.mark.parametrize((u'iterable', u'sequence'), [
    ([], Some(())),
    ([Some(1)], Some((1,))),
    ([Some(1), Some(2)], Some((1, 2))),
    ([Nothing, Some(1), Some(2)], Some((1, 2))),
    ([Some(1), Nothing, Some(2)], Some((1, 2))),
    ([Some(1), Some(2), Nothing], Some((1, 2))),
    ([Nothing], Some(())),

    ([], Success(())),
    ([Success(1)], Success((1,))),
    ([Success(1), Success(2)], Success((1, 2))),
    (
        [Failure(u'a'), Success(1), Success(2)],
        Success((1, 2)),
    ),
    ([Success(1), Failure(u'b')], Success((1,))),
    ([Failure(u'a'), Failure(u'b')], Success(())),

    ([], IOSuccess(())),
    ([IOSuccess(1)], IOSuccess((1,))),
    ([IOSuccess(1), IOSuccess(2)], IOSuccess((1, 2))),
    (
        [IOFailure(u'a'), IOSuccess(1), IOSuccess(2)],
        IOSuccess((1, 2)),
    ),
    ([IOSuccess(1), IOFailure(u'b')], IOSuccess((1,))),
    ([IOFailure(u'a'), IOFailure(u'b')], IOSuccess(())),
])
def test_collect_all_result(iterable, sequence):
    u"""Iterable for ``Result`` and ``Fold``."""
    assert Fold.collect_all(iterable, sequence.from_value(())) == sequence


@pytest.mark.parametrize((u'iterable', u'sequence'), [
    ([], ReaderResult.from_value(())),
    ([ReaderResult.from_value(1)], ReaderResult.from_value((1,))),
    (
        [ReaderResult.from_value(1), ReaderResult.from_value(2)],
        ReaderResult.from_value((1, 2)),
    ),
    (
        [
            ReaderResult.from_failure(u'a'),
            ReaderResult.from_value(1),
            ReaderResult.from_value(2),
        ],
        ReaderResult.from_value((1, 2)),
    ),
    (
        [ReaderResult.from_failure(u'a'), ReaderResult.from_failure(u'b')],
        ReaderResult.from_value(()),
    ),

    ([], ReaderIOResult.from_value(())),
    ([ReaderIOResult.from_value(1)], ReaderIOResult.from_value((1,))),
    (
        [ReaderIOResult.from_value(1), ReaderIOResult.from_value(2)],
        ReaderIOResult.from_value((1, 2)),
    ),
    (
        [
            ReaderIOResult.from_failure(u'a'),
            ReaderIOResult.from_value(1),
            ReaderIOResult.from_value(2),
        ],
        ReaderIOResult.from_value((1, 2)),
    ),
    (
        [ReaderIOResult.from_failure(u'a'), ReaderIOResult.from_failure(u'b')],
        ReaderIOResult.from_value(()),
    ),
])
def test_collect_all_reader_result(iterable, sequence):
    u"""Iterable for ``ReaderResult`` and ``Fold``."""
    assert Fold.collect_all(
        iterable, sequence.from_value(()),
    )(...) == sequence(...)


@pytest.mark.anyio()
async def test_collect_all_reader_future_result(subtests):
    u"""Iterable for ``ReaderFutureResult`` and ``Fold``."""
    containers: List[Tuple[  # noqa: WPS234
        Iterable[ReaderFutureResult[int, unicode, NoDeps]],
        ReaderFutureResult[Sequence[int], unicode, NoDeps],
    ]] = [
        ([], ReaderFutureResult.from_value(())),
        (
            [ReaderFutureResult.from_value(1)],
            ReaderFutureResult.from_value((1,)),
        ),
        (
            [
                ReaderFutureResult.from_value(1),
                ReaderFutureResult.from_value(2),
            ],
            ReaderFutureResult.from_value((1, 2)),
        ),
        (
            [
                ReaderFutureResult.from_failure(u'a'),
                ReaderFutureResult.from_value(1),
                ReaderFutureResult.from_value(2),
            ],
            ReaderFutureResult.from_value((1, 2)),
        ),
        (
            [
                ReaderFutureResult.from_failure(u'a'),
                ReaderFutureResult.from_failure(u'b'),
            ],
            ReaderFutureResult.from_value(()),
        ),
    ]
    for iterable, sequence in containers:
        with subtests.test(iterable=iterable, sequence=sequence):
            assert await Fold.collect_all(
                iterable, sequence.from_value(()),
            )(...) == await sequence(...)


@pytest.mark.anyio()
async def test_collect_all_future_result(subtests):
    u"""Iterable for ``FutureResult`` and ``Fold``."""
    containers: List[Tuple[  # noqa: WPS234
        Iterable[FutureResult[int, unicode]],
        FutureResult[Sequence[int], unicode],
    ]] = [
        ([], FutureSuccess(())),
        ([FutureSuccess(1)], FutureSuccess((1,))),
        ([FutureSuccess(1), FutureSuccess(2)], FutureSuccess((1, 2))),
        (
            [FutureFailure(u'a'), FutureSuccess(1), FutureSuccess(2)],
            FutureSuccess((1, 2)),
        ),
        ([FutureFailure(u'a'), FutureFailure(u'b')], FutureSuccess(())),
    ]
    for iterable, sequence in containers:
        with subtests.test(iterable=iterable, sequence=sequence):
            assert await Fold.collect_all(
                iterable, sequence.from_value(()),
            ) == await sequence


def test_fold_collect_recursion_limit():
    u"""Ensures that ``.collect_all`` method is recurion safe."""
    limit = sys.getrecursionlimit() + 1
    iterable = (Success(1) for _ in xrange(limit))
    expected = Success((1,) * limit)
    assert Fold.collect_all(iterable, Success(())) == expected
