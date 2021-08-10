from __future__ import absolute_import
from abc import ABCMeta
from functools import wraps
from inspect import FrameInfo
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    List,
    NoReturn,
    Optional,
    Type,
    TypeVar,
    Union,
)

from typing_extensions import final

from returns.interfaces.specific import result
from returns.primitives.container import BaseContainer, container_equality
from returns.primitives.exceptions import UnwrapFailedError
from returns.primitives.hkt import Kind2, SupportsKind2

# Definitions:
_ValueType = TypeVar(u'_ValueType', covariant=True)
_NewValueType = TypeVar(u'_NewValueType')
_ErrorType = TypeVar(u'_ErrorType', covariant=True)
_NewErrorType = TypeVar(u'_NewErrorType')

# Aliases:
_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')


class Result(
    BaseContainer,
    SupportsKind2[u'Result', _ValueType, _ErrorType],
    result.ResultBased2[_ValueType, _ErrorType],
):
    __metaclass__ = ABCMeta
    u"""
    Base class for :class:`~Failure` and :class:`~Success`.

    :class:`~Result` does not have a public constructor.
    Use :func:`~Success` and :func:`~Failure` to construct the needed values.

    See also:
        - https://bit.ly/361qQhi
        - https://hackernoon.com/the-throw-keyword-was-a-mistake-l9e532di

    """

    __slots__ = (u'_trace',)
    __match_args__ = (u'_inner_value',)

    _inner_value: Union[_ValueType, _ErrorType]
    _trace: Optional[List[FrameInfo]]

    # These two are required for projects like `classes`:
    #: Success type that is used to represent the successful computation.
    success_type: ClassVar[Type[u'Success']]
    #: Failure type that is used to represent the failed computation.
    failure_type: ClassVar[Type[u'Failure']]

    #: Typesafe equality comparison with other `Result` objects.
    equals = container_equality

    @property
    def trace(self):
        u"""Returns a list with stack trace when :func:`~Failure` was called."""
        return self._trace

    def swap(self):
        u"""
        Swaps value and error types.

        So, values become errors and errors become values.
        It is useful when you have to work with errors a lot.
        And since we have a lot of ``.bind_`` related methods
        and only a single ``.lash`` - it is easier to work with values.

        .. code:: python

          >>> from returns.result import Success, Failure
          >>> assert Success(1).swap() == Failure(1)
          >>> assert Failure(1).swap() == Success(1)

        """

    def map(
        self,
        function,
    ):
        u"""
        Composes successful container with a pure function.

        .. code:: python

          >>> from returns.result import Failure, Success

          >>> def mappable(string: str) -> str:
          ...      return string + 'b'

          >>> assert Success('a').map(mappable) == Success('ab')
          >>> assert Failure('a').map(mappable) == Failure('a')

        """

    def apply(
        self,
        container,
    ):
        u"""
        Calls a wrapped function in a container on this container.

        .. code:: python

          >>> from returns.result import Failure, Success

          >>> def appliable(string: str) -> str:
          ...      return string + 'b'

          >>> assert Success('a').apply(Success(appliable)) == Success('ab')
          >>> assert Failure('a').apply(Success(appliable)) == Failure('a')

          >>> assert Success('a').apply(Failure(1)) == Failure(1)
          >>> assert Failure(1).apply(Failure(2)) == Failure(1)

        """

    def bind(
        self,
        function,
    ):
        u"""
        Composes successful container with a function that returns a container.

        .. code:: python

          >>> from returns.result import Result, Success, Failure

          >>> def bindable(arg: str) -> Result[str, str]:
          ...      if len(arg) > 1:
          ...          return Success(arg + 'b')
          ...      return Failure(arg + 'c')

          >>> assert Success('aa').bind(bindable) == Success('aab')
          >>> assert Success('a').bind(bindable) == Failure('ac')
          >>> assert Failure('a').bind(bindable) == Failure('a')

        """

    #: Alias for `bind_result` method, it is the same as `bind` here.
    bind_result = bind

    def alt(
        self,
        function,
    ):
        u"""
        Composes failed container with a pure function to modify failure.

        .. code:: python

          >>> from returns.result import Failure, Success

          >>> def altable(arg: str) -> str:
          ...      return arg + 'b'

          >>> assert Success('a').alt(altable) == Success('a')
          >>> assert Failure('a').alt(altable) == Failure('ab')

        """

    def lash(
        self,
        function,
    ):
        u"""
        Composes failed container with a function that returns a container.

        .. code:: python

          >>> from returns.result import Result, Success, Failure

          >>> def lashable(arg: str) -> Result[str, str]:
          ...      if len(arg) > 1:
          ...          return Success(arg + 'b')
          ...      return Failure(arg + 'c')

          >>> assert Success('a').lash(lashable) == Success('a')
          >>> assert Failure('a').lash(lashable) == Failure('ac')
          >>> assert Failure('aa').lash(lashable) == Success('aab')

        """

    def value_or(
        self,
        default_value,
    ):
        u"""
        Get value or default value.

        .. code:: python

          >>> from returns.result import Failure, Success
          >>> assert Success(1).value_or(2) == 1
          >>> assert Failure(1).value_or(2) == 2

        """

    def unwrap(self):
        u"""
        Get value or raise exception.

        .. code:: pycon
          :force:

          >>> from returns.result import Failure, Success
          >>> assert Success(1).unwrap() == 1

          >>> Failure(1).unwrap()
          Traceback (most recent call last):
            ...
          returns.primitives.exceptions.UnwrapFailedError

        """  # noqa: RST307

    def failure(self):
        u"""
        Get failed value or raise exception.

        .. code:: pycon
          :force:

          >>> from returns.result import Failure, Success
          >>> assert Failure(1).failure() == 1

          >>> Success(1).failure()
          Traceback (most recent call last):
            ...
          returns.primitives.exceptions.UnwrapFailedError

        """  # noqa: RST307

    @classmethod
    def from_value(
        cls, inner_value,
    ):
        u"""
        One more value to create success unit values.

        It is useful as a united way to create a new value from any container.

        .. code:: python

          >>> from returns.result import Result, Success
          >>> assert Result.from_value(1) == Success(1)

        You can use this method or :func:`~Success`,
        choose the most convenient for you.

        """
        return Success(inner_value)

    @classmethod
    def from_failure(
        cls, inner_value,
    ):
        u"""
        One more value to create failure unit values.

        It is useful as a united way to create a new value from any container.

        .. code:: python

          >>> from returns.result import Result, Failure
          >>> assert Result.from_failure(1) == Failure(1)

        You can use this method or :func:`~Failure`,
        choose the most convenient for you.

        """
        return Failure(inner_value)

    @classmethod
    def from_result(
        cls, inner_value,
    ):
        u"""
        Creates a new ``Result`` instance from existing ``Result`` instance.

        .. code:: python

          >>> from returns.result import Result, Failure, Success
          >>> assert Result.from_result(Success(1)) == Success(1)
          >>> assert Result.from_result(Failure(1)) == Failure(1)

        This is a part of
        :class:`returns.interfaces.specific.result.ResultBasedN` interface.
        """
        return inner_value


class Failure(Result[Any, _ErrorType]):  # noqa: WPS338
    u"""
    Represents a calculation which has failed.

    It should contain an error code or message.
    """

    _inner_value: _ErrorType

    def __init__(self, inner_value):
        u"""Failure constructor."""
        super(Failure, self).__init__(inner_value)
        object.__setattr__(self, u'_trace', self._get_trace())  # noqa: WPS609

    if not TYPE_CHECKING:  # noqa: C901, WPS604  # pragma: no branch
        def alt(self, function):
            u"""Composes failed container with a pure function to modify failure."""  # noqa: E501
            return Failure(function(self._inner_value))

        def map(self, function):
            u"""Does nothing for ``Failure``."""
            return self

        def bind(self, function):
            u"""Does nothing for ``Failure``."""
            return self

        #: Alias for `bind` method. Part of the `ResultBasedN` interface.
        bind_result = bind

        def lash(self, function):
            u"""Composes this container with a function returning container."""
            return function(self._inner_value)

        def apply(self, container):
            u"""Does nothing for ``Failure``."""
            return self

        def value_or(self, default_value):
            u"""Returns default value for failed container."""
            return default_value

    def swap(self):
        u"""Failures swap to :class:`Success`."""
        return Success(self._inner_value)

    def unwrap(self):
        u"""Raises an exception, since it does not have a value inside."""
        if isinstance(self._inner_value, Exception):
            raise UnwrapFailedError(self)
        raise UnwrapFailedError(self)

    def failure(self):
        u"""Returns failed value."""
        return self._inner_value

    def _get_trace(self):
        u"""Method that will be monkey patched when trace is active."""
        return None  # noqa: WPS324


Failure = final  # noqa: WPS338(Failure)

class Success(Result[_ValueType, Any]):
    u"""
    Represents a calculation which has succeeded and contains the result.

    Contains the computation value.
    """

    _inner_value: _ValueType

    def __init__(self, inner_value):
        u"""Success constructor."""
        super(Success, self).__init__(inner_value)

    if not TYPE_CHECKING:  # noqa: C901, WPS604  # pragma: no branch
        def alt(self, function):
            u"""Does nothing for ``Success``."""
            return self

        def map(self, function):
            u"""Composes current container with a pure function."""
            return Success(function(self._inner_value))

        def bind(self, function):
            u"""Binds current container to a function that returns container."""
            return function(self._inner_value)

        #: Alias for `bind` method. Part of the `ResultBasedN` interface.
        bind_result = bind

        def lash(self, function):
            u"""Does nothing for ``Success``."""
            return self

        def apply(self, container):
            u"""Calls a wrapped function in a container on this container."""
            if isinstance(container, self.success_type):
                return self.map(container.unwrap())
            return container

        def value_or(self, default_value):
            u"""Returns the value for successful container."""
            return self._inner_value

    def swap(self):
        u"""Successes swap to :class:`Failure`."""
        return Failure(self._inner_value)

    def unwrap(self):
        u"""Returns the unwrapped value from successful container."""
        return self._inner_value

    def failure(self):
        u"""Raises an exception for successful container."""
        raise UnwrapFailedError(self)


Success = final(Success)

Result.success_type = Success
Result.failure_type = Failure

# Aliases:

#: Alias for a popular case when ``Result`` has ``Exception`` as error type.
ResultE = Result[_ValueType, Exception]


# Decorators:

def safe(
    function,
):
    u"""
    Decorator to convert exception-throwing function to ``Result`` container.

    Should be used with care, since it only catches ``Exception`` subclasses.
    It does not catch ``BaseException`` subclasses.

    If you need to mark ``async`` function as ``safe``,
    use :func:`returns.future.future_safe` instead.
    This decorator only works with sync functions. Example:

    .. code:: python

      >>> from returns.result import Result, Success, safe

      >>> @safe
      ... def might_raise(arg: int) -> float:
      ...     return 1 / arg

      >>> assert might_raise(1) == Success(1.0)
      >>> assert isinstance(might_raise(0), Result.failure_type)

    Similar to :func:`returns.io.impure_safe`
    and :func:`returns.future.future_safe` decorators.

    Requires our :ref:`mypy plugin <mypy-plugins>`.

    """
    @wraps(function)
    def decorator(*args, **kwargs):
        try:
            return Success(function(*args, **kwargs))
        except Exception, exc:
            return Failure(exc)
    return decorator
