from __future__ import absolute_import
from returns.result import Failure, ResultE, Success


def test_result_error_success():
    u"""Ensures that ResultE can be typecasted to success."""
    container: ResultE[int] = Success(1)
    assert container.unwrap() == 1


def test_result_error_failure():
    u"""Ensures that ResultE can be typecasted to failure."""
    container: ResultE[int] = Failure(ValueError(u'1'))
    assert unicode(container.failure()) == u'1'
