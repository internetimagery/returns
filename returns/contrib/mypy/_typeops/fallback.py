from __future__ import absolute_import
from functools import wraps
from typing import Callable, TypeVar

from mypy.types import AnyType, TypeOfAny

_CallableType = TypeVar(u'_CallableType', bound=Callable)


def asserts_fallback_to_any(function):
    u"""
    Falls back to ``Any`` when some ``assert ...`` fails in our plugin code.

    We often use ``assert isinstance(variable, Instance)``
    as a way to ensure correctness in this plugin.
    But, we need a generic way to handle all
    possible exceptions in a single manner:
    just return ``Any`` and hope that someday someone reports it.

    """
    @wraps(function)
    def decorator(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except AssertionError:
            # TODO: log it somehow
            return AnyType(TypeOfAny.implementation_artifact)
    return decorator  # type: ignore
