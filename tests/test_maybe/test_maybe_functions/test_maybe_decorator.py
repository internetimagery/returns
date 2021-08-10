from __future__ import absolute_import
from typing import Dict, Optional

from returns.maybe import Nothing, Some, maybe


@maybe
def _function(hashmap, key):
    return hashmap.get(key, None)


def test_maybe_some():
    u"""Ensures that maybe decorator works correctly for some case."""
    assert _function({u'a': u'b'}, u'a') == Some(u'b')


def test_maybe_nothing():
    u"""Ensures that maybe decorator works correctly for nothing case."""
    assert _function({u'a': u'b'}, u'c') == Nothing
