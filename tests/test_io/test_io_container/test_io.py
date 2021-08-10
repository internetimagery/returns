from __future__ import division
from __future__ import absolute_import
import pytest

from returns.io import IO, IOFailure, IOResult, IOSuccess


def test_io_map():
    u"""Ensures that IO container supports ``.map()`` method."""
    io: IO[float] = IO(1).map(
        lambda number: number / 2,
    )

    assert io == IO(0.5)


def test_io_bind():
    u"""Ensures that IO container supports ``.bind()`` method."""
    io: IO[int] = IO(u'1').bind(
        lambda number: IO(int(number)),
    )

    assert io == IO(1)


def test_io_str():
    u"""Ensures that IO container supports str cast."""
    assert unicode(IO([])) == u'<IO: []>'


@pytest.mark.parametrize(u'container', [
    IOSuccess(1),
    IOFailure(1),
])
def test_io_typecast_reverse(container):
    u"""Ensures that IO can be casted to IOResult and back."""
    assert IO.from_ioresult(container) == IO.from_ioresult(
        IOResult.from_typecast(IO.from_ioresult(container)),
    )
