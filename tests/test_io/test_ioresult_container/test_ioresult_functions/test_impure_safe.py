
from __future__ import division
from __future__ import absolute_import
from returns.io import IOSuccess, impure_safe


@impure_safe
def _function(number):
    return number / number


def test_safe_iosuccess():
    u"""Ensures that safe decorator works correctly for IOSuccess case."""
    assert _function(1) == IOSuccess(1.0)


def test_safe_iofailure():
    u"""Ensures that safe decorator works correctly for IOFailure case."""
    failed = _function(0)
    assert isinstance(
        failed.failure()._inner_value, ZeroDivisionError,  # noqa: WPS437
    )
