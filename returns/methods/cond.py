from __future__ import absolute_import
from typing import Optional, Type, TypeVar, Union, overload

from returns.context import NoDeps
from returns.interfaces.failable import DiverseFailableN, SingleFailableN
from returns.primitives.hkt import KindN, kinded

_ValueType = TypeVar(u'_ValueType')
_ErrorType = TypeVar(u'_ErrorType')

_SingleFailableKind = TypeVar(u'_SingleFailableKind', bound=SingleFailableN)
_DiverseFailableKind = TypeVar(u'_DiverseFailableKind', bound=DiverseFailableN)


@overload
def internal_cond(
    container_type,
    is_success,
    success_value,
):
    u"""Reduce the boilerplate when choosing paths with ``SingleFailableN``."""


@overload
def internal_cond(
    container_type,
    is_success,
    success_value,
    error_value,
):
    u"""Reduce the boilerplate when choosing paths with ``DiverseFailableN``."""


def internal_cond(  # type: ignore
    container_type,
    is_success,
    success_value,
    error_value = None,
):
    u"""
    Reduce the boilerplate when choosing paths.

    Works with ``SingleFailableN`` (e.g. ``Maybe``)
    and ``DiverseFailableN`` (e.g. ``Result``).

    Example using ``cond`` with the ``Result`` container:

    .. code:: python

      >>> from returns.methods import cond
      >>> from returns.result import Failure, Result, Success

      >>> def is_numeric(string: str) -> Result[str, str]:
      ...     return cond(
      ...         Result,
      ...         string.isnumeric(),
      ...         'It is a number',
      ...         'It is not a number',
      ...     )

      >>> assert is_numeric('42') == Success('It is a number')
      >>> assert is_numeric('non numeric') == Failure('It is not a number')

    Example using ``cond`` with the ``Maybe`` container:

    .. code:: python

      >>> from returns.maybe import Maybe, Some, Nothing

      >>> def is_positive(number: int) -> Maybe[int]:
      ...     return cond(Maybe, number > 0, number)

      >>> assert is_positive(10) == Some(10)
      >>> assert is_positive(-10) == Nothing

    """
    if is_success:
        return container_type.from_value(success_value)

    if issubclass(container_type, DiverseFailableN):
        return container_type.from_failure(error_value)
    return container_type.empty  # type: ignore


#: Kinded version of :func:`~internal_cond`, use it to infer real return type.
cond = kinded(internal_cond)
