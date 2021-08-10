from __future__ import absolute_import
from typing import Callable, Optional, Type, TypeVar, Union, overload

from returns.context import NoDeps
from returns.interfaces.failable import DiverseFailableN, SingleFailableN
from returns.methods.cond import internal_cond
from returns.primitives.hkt import Kinded, KindN

_ValueType = TypeVar(u'_ValueType')
_ErrorType = TypeVar(u'_ErrorType')

_DiverseFailableKind = TypeVar(u'_DiverseFailableKind', bound=DiverseFailableN)
_SingleFailableKind = TypeVar(u'_SingleFailableKind', bound=SingleFailableN)


@overload
def cond(
    container_type,
    success_value,
):
    u"""Reduce the boilerplate when choosing paths with ``SingleFailableN``."""


@overload
def cond(
    container_type,
    success_value,
    error_value,
):
    u"""Reduce the boilerplate when choosing paths with ``DiverseFailableN``."""


def cond(  # type: ignore
    container_type,
    success_value,
    error_value = None,
):
    u"""
    Reduce the boilerplate when choosing paths.

    Works with ``SingleFailableN`` (e.g. ``Maybe``)
    and ``DiverseFailableN`` (e.g. ``Result``).

    Example using ``cond`` with the ``Result`` container:

    .. code:: python

      >>> from returns.pointfree import cond
      >>> from returns.result import Failure, Result, Success

      >>> assert cond(Result, 'success', 'failure')(True) == Success('success')
      >>> assert cond(Result, 'success', 'failure')(False) == Failure('failure')

    Example using ``cond`` with the ``Maybe`` container:

    .. code:: python

      >>> from returns.maybe import Maybe, Some, Nothing

      >>> assert cond(Maybe, 10.0)(True) == Some(10.0)
      >>> assert cond(Maybe, 10.0)(False) == Nothing

    """
    def factory(is_success):
        return internal_cond(
            container_type, is_success, success_value, error_value,
        )
    return factory
