
from __future__ import absolute_import
from returns.io import IO, impure


def _fake_impure_function(some_param):
    return some_param


def test_impure():
    u"""Ensures that impure returns IO container."""
    impure_result = impure(_fake_impure_function)(1)
    assert isinstance(impure_result, IO)
    assert impure_result == IO(1)
