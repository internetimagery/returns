from __future__ import with_statement
from __future__ import absolute_import
import sys
from typing import Iterable, List, Sequence, Tuple

import pytest

from returns.context import (
    NoDeps,
    Reader,
    ReaderFutureResult,
    ReaderIOResult,
    ReaderResult,
)
from returns.future import Future, FutureFailure, FutureResult, FutureSuccess
from returns.io import IO, IOFailure, IOSuccess
from returns.iterables import Fold
from returns.maybe import Nothing, Some
from returns.result import Failure, Success


@pytest.mark.parametrize((u'iterable', u'sequence'), [
    # Regular types:

    ([], IO(())),
    ([IO(1)], IO((1,))),
    ([IO(1), IO(2)], IO((1, 2))),

    # Can fail:

    ([], Success(())),
    ([Success(1)], Success((1,))),
    ([Success(1), Success(2)], Success((1, 2))),
    (
        [Failure(u'a'), Success(1), Success(2)],
        Failure(u'a'),
    ),
    ([Success(1), Failure(u'a')], Failure(u'a')),
    ([Failure(u'a'), Failure(u'b')], Failure(u'a')),

    ([], Some(())),
    ([Some(1)], Some((1,))),
    ([Some(1), Some(2)], Some((1, 2))),
    ([Nothing, Some(1), Some(2)], Nothing),
    ([Some(1), Nothing, Some(2)], Nothing),
    ([Some(1), Some(2), Nothing], Nothing),
    ([Nothing], Nothing),

    ([], IOSuccess(())),
    ([IOSuccess(1)], IOSuccess((1,))),
    ([IOSuccess(1), IOSuccess(2)], IOSuccess((1, 2))),
    (
        [IOFailure(u'a'), IOSuccess(1), IOSuccess(2)],
        IOFailure(u'a'),
    ),
    ([IOSuccess(1), IOFailure(u'a')], IOFailure(u'a')),
    ([IOFailure(u'a'), IOFailure(u'b')], IOFailure(u'a')),
])
def test_fold_collect(iterable, sequence):
    u"""Iterable for regular types and ``Fold``."""
    assert Fold.collect(iterable, sequence.from_value(())) == sequence


@pytest.mark.parametrize((u'iterable', u'sequence'), [
    # Regular types:

    ([], Reader.from_value(())),
    ([Reader.from_value(1)], Reader.from_value((1,))),
    (
        [Reader.from_value(1), Reader.from_value(2)],
        Reader.from_value((1, 2)),
    ),

    # Can fail:

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
        ReaderResult.from_failure(u'a'),
    ),
    (
        [ReaderResult.from_failure(u'a'), ReaderResult.from_failure(u'b')],
        ReaderResult.from_failure(u'a'),
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
        ReaderIOResult.from_failure(u'a'),
    ),
    (
        [ReaderIOResult.from_failure(u'a'), ReaderIOResult.from_failure(u'b')],
        ReaderIOResult.from_failure(u'a'),
    ),
])
def test_fold_collect_reader(iterable, sequence):
    u"""Ensures that ``.collect`` works for readers."""
    assert Fold.collect(
        iterable,
        sequence.from_value(()),
    )(...) == sequence(...)


@pytest.mark.anyio()
async def test_fold_collect_reader_future_result(subtests):
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
            ReaderFutureResult.from_failure(u'a'),
        ),
        (
            [
                ReaderFutureResult.from_failure(u'a'),
                ReaderFutureResult.from_failure(u'b'),
            ],
            ReaderFutureResult.from_failure(u'a'),
        ),
    ]
    for iterable, sequence in containers:
        with subtests.test(iterable=iterable, sequence=sequence):
            assert await Fold.collect(
                iterable, sequence.from_value(()),
            )(...) == await sequence(...)


@pytest.mark.anyio()
async def test_fold_collect_future(subtests):
    u"""Iterable for ``Future`` and ``Fold``."""
    containers: List[Tuple[  # noqa: WPS234
        Iterable[Future[int]],
        Future[Sequence[int]],
    ]] = [
        ([], Future.from_value(())),
        ([Future.from_value(1)], Future.from_value((1,))),
        (
            [Future.from_value(1), Future.from_value(2)],
            Future.from_value((1, 2)),
        ),
    ]
    for iterable, sequence in containers:
        with subtests.test(iterable=iterable, sequence=sequence):
            assert await Fold.collect(
                iterable, sequence.from_value(()),
            ) == await sequence


@pytest.mark.anyio()
async def test_fold_collect_future_result(subtests):
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
            FutureFailure(u'a'),
        ),
        ([FutureFailure(u'a'), FutureFailure(u'b')], FutureFailure(u'a')),
    ]
    for iterable, sequence in containers:
        with subtests.test(iterable=iterable, sequence=sequence):
            assert await Fold.collect(
                iterable, sequence.from_value(()),
            ) == await sequence


def test_fold_collect_recursion_limit():
    u"""Ensures that ``.collect`` method is recurion safe."""
    limit = sys.getrecursionlimit() + 1
    iterable = (IO(1) for _ in xrange(limit))
    expected = IO((1,) * limit)
    assert Fold.collect(iterable, IO(())) == expected
