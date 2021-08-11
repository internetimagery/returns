from __future__ import absolute_import
from typing import Any, Callable, NoReturn, TypeVar

from six import wraps

# Aliases:
_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')


def identity(instance):
    u"""
    Function that returns its argument.

    .. code:: python

      >>> assert identity(1) == 1
      >>> assert identity([1, 2, 3]) == [1, 2, 3]

    This function is really helpful for some composition.
    It is also useful for "do nothing" use-case.

    See also:
        - https://en.wikipedia.org/wiki/Identity_function
        - https://stackoverflow.com/a/21506571/4842742

    """
    return instance


def compose(
    first,
    second,
):
    u"""
    Allows function composition.

    Works as: ``second . first`` or ``first() |> second()``.
    You can read it as "second after first".

    .. code:: python

      >>> assert compose(float, int)('123.5') == 123

    We can only compose functions with one argument and one return.
    Type checked.
    """
    return lambda argument: second(first(argument))


def tap(
    function,
):
    u"""
    Allows to apply some function and return an argument, instead of a result.

    Is useful for composing functions with
    side-effects like ``print()``, ``logger.log()``, etc.

    .. code:: python

      >>> assert tap(print)(1) == 1
      1
      >>> assert tap(lambda _: 1)(2) == 2

    See also:
        - https://github.com/dry-python/returns/issues/145

    """
    def decorator(argument_to_return):
        function(argument_to_return)
        return argument_to_return
    return decorator


def untap(
    function,
):
    u"""
    Allows to apply some function and always return ``None`` as a result.

    Is useful for composing functions that do some side effects
    and return some nosense.

    Is the kind of a reverse of the ``tap`` function.

    .. code:: python

      >>> def strange_log(arg: int) -> int:
      ...     print(arg)
      ...     return arg

      >>> assert untap(strange_log)(2) is None
      2
      >>> assert untap(tap(lambda _: 1))(2) is None

    See also:
        - https://github.com/dry-python/returns/issues/145

    """
    def decorator(argument_to_return):
        function(argument_to_return)
    return decorator


def raise_exception(exception):
    u"""
    Helper function to raise exceptions as a function.

    It might be required as a compatibility tool for existing APIs.
    That's how it can be used:

    .. code:: pycon

      >>> from returns.result import Failure, Result
      >>> # Some operation result:
      >>> user: Result[int, ValueError] = Failure(ValueError('boom'))

      >>> # Here we unwrap internal exception and raise it:
      >>> user.alt(raise_exception)
      Traceback (most recent call last):
        ...
      ValueError: boom

    See also:
        - https://github.com/dry-python/returns/issues/56

    """
    raise exception


def not_(function):
    u"""
    Denies the function returns.

    .. code:: python

      >>> from returns.result import Result, Success, Failure

      >>> def is_successful(result_container: Result[float, int]) -> bool:
      ...     return isinstance(result_container, Result.success_type)

      >>> assert not_(is_successful)(Success(1.0)) is False
      >>> assert not_(is_successful)(Failure(1)) is True

    """
    @wraps(function)  # noqa: WPS430
    def wrapped_function(*args, **kwargs):  # noqa: WPS430
        return not function(*args, **kwargs)
    return wrapped_function
