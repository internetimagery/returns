from __future__ import absolute_import
from returns.io import IOFailure, IOSuccess


def test_map_iosuccess():
    u"""Ensures that IOSuccess is mappable."""
    assert IOSuccess(5).map(unicode) == IOSuccess(u'5')


def test_alt_iofailure():
    u"""Ensures that IOFailure is mappable."""
    assert IOFailure(5).map(unicode) == IOFailure(5)
    assert IOFailure(5).alt(unicode) == IOFailure(u'5')


def test_alt_iosuccess():
    u"""Ensures that IOSuccess.alt is NoOp."""
    assert IOSuccess(5).alt(unicode) == IOSuccess(5)
