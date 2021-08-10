from __future__ import with_statement
from __future__ import absolute_import
import sys
from typing import Iterable, List, Tuple

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


def _sum_two(first):
    return lambda second: first + second


@pytest.mark.parametrize((u'iterable', u'sequence'), [
    # Regular types:

    ([], IO(10)),
    ([IO(1)], IO(11)),
    ([IO(1), IO(2)], IO(13)),

    # Can fail:

    ([], Success(10)),
    ([Success(1)], Success(11)),
    ([Success(1), Success(2)], Success(13)),
    (
        [Failure(u'a'), Success(1), Success(2)],
        Failure(u'a'),
    ),
    ([Success(1), Failure(u'a')], Failure(u'a')),
    ([Failure(u'a'), Failure(u'b')], Failure(u'a')),

    ([], Some(10)),
    ([Some(1)], Some(11)),
    ([Some(1), Some(2)], Some(13)),
    ([Nothing, Some(1), Some(2)], Nothing),
    ([Some(1), Nothing, Some(2)], Nothing),
    ([Some(1), Some(2), Nothing], Nothing),
    ([Nothing], Nothing),

    ([], IOSuccess(10)),
    ([IOSuccess(1)], IOSuccess(11)),
    ([IOSuccess(1), IOSuccess(2)], IOSuccess(13)),
    (
        [IOFailure(u'a'), IOSuccess(1), IOSuccess(2)],
        IOFailure(u'a'),
    ),
    ([IOFailure(u'a'), IOFailure(u'b')], IOFailure(u'a')),
])
def test_fold_loop(iterable, sequence):
    u"""Iterable for ``Result`` and ``FailFast``."""
    assert Fold.loop(iterable, sequence.from_value(10), _sum_two) == sequence


@pytest.mark.parametrize((u'iterable', u'sequence'), [
    # Regular types:

    ([], Reader.from_value(10)),
    ([Reader.from_value(1)], Reader.from_value(11)),
    (
        [Reader.from_value(1), Reader.from_value(2)],
        Reader.from_value(13),
    ),

    # Can fail:

    ([], ReaderResult.from_value(10)),
    ([ReaderResult.from_value(1)], ReaderResult.from_value(11)),
    (
        [ReaderResult.from_value(1), ReaderResult.from_value(2)],
        ReaderResult.from_value(13),
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

    ([], ReaderIOResult.from_value(10)),
    ([ReaderIOResult.from_value(1)], ReaderIOResult.from_value(11)),
    (
        [ReaderIOResult.from_value(1), ReaderIOResult.from_value(2)],
        ReaderIOResult.from_value(13),
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
    (
        [ReaderIOResult.from_value(1), ReaderIOResult.from_failure(u'a')],
        ReaderIOResult.from_failure(u'a'),
    ),
])
def test_fold_loop_reader(iterable, sequence):
    u"""Ensures that ``.loop`` works for readers."""
    assert Fold.loop(
        iterable,
        sequence.from_value(10),
        _sum_two,
    )(...) == sequence(...)


@pytest.mark.anyio()
async def test_fold_loop_reader_future_result(subtests):
    u"""Iterable for ``ReaderFutureResult`` and ``Fold``."""
    containers: List[Tuple[  # noqa: WPS234
        Iterable[ReaderFutureResult[int, unicode, NoDeps]],
        ReaderFutureResult[int, unicode, NoDeps],
    ]] = [
        ([], ReaderFutureResult.from_value(10)),
        (
            [ReaderFutureResult.from_value(1)],
            ReaderFutureResult.from_value(11),
        ),
        (
            [
                ReaderFutureResult.from_value(1),
                ReaderFutureResult.from_value(2),
            ],
            ReaderFutureResult.from_value(13),
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
        (
            [
                ReaderFutureResult.from_value(1),
                ReaderFutureResult.from_failure(u'a'),
            ],
            ReaderFutureResult.from_failure(u'a'),
        ),
    ]
    for iterable, sequence in containers:
        with subtests.test(iterable=iterable, sequence=sequence):
            assert await Fold.loop(
                iterable, sequence.from_value(10), _sum_two,
            )(...) == await sequence(...)


@pytest.mark.anyio()
async def test_fold_collect_future(subtests):
    u"""Iterable for ``Future`` and ``Fold``."""
    containers: List[Tuple[  # noqa: WPS234
        Iterable[Future[int]],
        Future[int],
    ]] = [
        ([], Future.from_value(10)),
        ([Future.from_value(1)], Future.from_value(11)),
        (
            [Future.from_value(1), Future.from_value(2)],
            Future.from_value(13),
        ),
    ]
    for iterable, sequence in containers:
        with subtests.test(iterable=iterable, sequence=sequence):
            assert await Fold.loop(
                iterable, sequence.from_value(10), _sum_two,
            ) == await sequence


@pytest.mark.anyio()
async def test_fold_collect_future_result(subtests):
    u"""Iterable for ``FutureResult`` and ``Fold``."""
    containers: List[Tuple[  # noqa: WPS234
        Iterable[FutureResult[int, unicode]],
        FutureResult[int, unicode],
    ]] = [
        ([], FutureSuccess(10)),
        ([FutureSuccess(1)], FutureSuccess(11)),
        ([FutureSuccess(1), FutureSuccess(2)], FutureSuccess(13)),
        (
            [FutureFailure(u'a'), FutureSuccess(1), FutureSuccess(2)],
            FutureFailure(u'a'),
        ),
        ([FutureFailure(u'a'), FutureFailure(u'b')], FutureFailure(u'a')),
        ([FutureSuccess(1), FutureFailure(u'a')], FutureFailure(u'a')),
    ]
    for iterable, sequence in containers:
        with subtests.test(iterable=iterable, sequence=sequence):
            assert await Fold.loop(
                iterable, sequence.from_value(10), _sum_two,
            ) == await sequence


def test_fold_loop_recursion_limit():
    u"""Ensures that ``.loop`` method is recurion safe."""
    limit = sys.getrecursionlimit() + 1
    iterable = (IO(1) for _ in xrange(limit))
    assert Fold.loop(iterable, IO(0), _sum_two) == IO(limit)
