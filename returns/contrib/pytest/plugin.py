from __future__ import absolute_import
import inspect
import sys
from contextlib import contextmanager
from functools import partial, wraps
from types import FrameType
from typing import TYPE_CHECKING, Any, Callable, Iterator, TypeVar, Union

import pytest
from typing_extensions import Final, final

if TYPE_CHECKING:
    from returns.interfaces.specific.result import ResultLikeN

_ERROR_FIELD: Final = u'_error_handled'
_ERROR_HANDLERS: Final = (
    u'lash',
)
_ERRORS_COPIERS: Final = (
    u'map',
    u'alt',
)

_FunctionType = TypeVar(u'_FunctionType', bound=Callable)
_ReturnsResultType = TypeVar(
    u'_ReturnsResultType',
    bound=Union[u'ResultLikeN', Callable[..., u'ResultLikeN']],
)


class ReturnsAsserts(object):
    u"""Class with helpers assertions to check containers."""

    __slots__ = ()

    def assert_equal(
        self,
        first,
        second, **_3to2kwargs
    ):
        if 'backend' in _3to2kwargs: backend = _3to2kwargs['backend']; del _3to2kwargs['backend']
        else: backend =  u'asyncio'
        if 'deps' in _3to2kwargs: deps = _3to2kwargs['deps']; del _3to2kwargs['deps']
        else: deps = None
        u"""Can compare two containers even with extra calling and awaiting."""
        from returns.primitives.asserts import assert_equal
        assert_equal(first, second, deps=deps, backend=backend)

    def is_error_handled(self, container):
        u"""Ensures that container has its error handled in the end."""
        return bool(getattr(container, _ERROR_FIELD, False))

    @contextmanager
    def assert_trace(
        self,
        trace_type,
        function_to_search,
    ):
        u"""
        Ensures that a given function was called during execution.

        Use it to determine where the failure happened.
        """
        old_tracer = sys.gettrace()
        sys.settrace(partial(_trace_function, trace_type, function_to_search))

        try:
            yield
        except _DesiredFunctionFound:
            pass  # noqa: WPS420
        else:
            pytest.fail(
                u'No container {0} was created'.format(trace_type.__name__),
            )
        finally:
            sys.settrace(old_tracer)


ReturnsAsserts = final(ReturnsAsserts)

@pytest.fixture(scope=u'session')
def returns(_patch_containers):  # noqa: WPS442
    u"""Returns our own class with helpers assertions to check containers."""
    return ReturnsAsserts()


def pytest_configure(config):
    u"""
    Hook to be executed on import.

    We use it define custom markers.
    """
    config.addinivalue_line(
        u'markers',
        (
            u'returns_lawful: all tests under `check_all_laws` ' +
            u'is marked this way, ' +
            u'use `-m "not returns_lawful"` to skip them.'
        ),
    )


@pytest.fixture(scope=u'session')
def _patch_containers():
    u"""
    Fixture to add test specifics into our containers.

    Currently we inject:

    - Error handling state, this is required to test that ``Result``-based
      containers do handle errors

    Even more things to come!
    """
    _patch_error_handling(_ERROR_HANDLERS, _PatchedContainer.error_handler)
    _patch_error_handling(_ERRORS_COPIERS, _PatchedContainer.copy_handler)


def _patch_error_handling(methods, patch_handler):
    for container in _PatchedContainer.containers_to_patch():
        for method in methods:
            original = getattr(container, method, None)
            if original:
                setattr(container, method, patch_handler(original))


def _trace_function(
    trace_type,
    function_to_search,
    frame,
    event,
    arg,
):
    is_desired_type_call = (
        event == u'call' and
        (
            # Some containers is created through functions and others
            # is created directly using class constructors!
            # The first line covers when it's created through a function
            # The second line covers when it's created through a
            # class constructor
            frame.f_code is getattr(trace_type, u'__code__', None) or
            frame.f_code is getattr(trace_type.__init__, u'__code__', None)  # type: ignore[misc]  # noqa: E501
        )
    )
    if is_desired_type_call:
        current_call_stack = inspect.stack()
        function_to_search_code = getattr(function_to_search, u'__code__', None)
        for frame_info in current_call_stack:
            if function_to_search_code is frame_info.frame.f_code:
                raise _DesiredFunctionFound()


class _PatchedContainer(object):
    u"""Class with helper methods to patched containers."""

    __slots__ = ()

    @classmethod
    def containers_to_patch(cls):
        u"""We need this method so coverage will work correctly."""
        from returns.context import (
            RequiresContextFutureResult,
            RequiresContextIOResult,
            RequiresContextResult,
        )
        from returns.future import FutureResult
        from returns.io import IOFailure, IOSuccess
        from returns.result import Failure, Success

        return (
            Success,
            Failure,
            IOSuccess,
            IOFailure,
            RequiresContextResult,
            RequiresContextIOResult,
            RequiresContextFutureResult,
            FutureResult,
        )

    @classmethod
    def error_handler(cls, original):
        if inspect.iscoroutinefunction(original):
            async def factory(self, *args, **kwargs):
                original_result = await original(self, *args, **kwargs)
                object.__setattr__(
                    original_result, _ERROR_FIELD, True,  # noqa: WPS425
                )
                return original_result
        else:
            def factory(self, *args, **kwargs):
                original_result = original(self, *args, **kwargs)
                object.__setattr__(
                    original_result, _ERROR_FIELD, True,  # noqa: WPS425
                )
                return original_result
        return wraps(original)(factory)

    @classmethod
    def copy_handler(cls, original):
        if inspect.iscoroutinefunction(original):
            async def factory(self, *args, **kwargs):
                original_result = await original(self, *args, **kwargs)
                object.__setattr__(
                    original_result,
                    _ERROR_FIELD,
                    getattr(self, _ERROR_FIELD, False),
                )
                return original_result
        else:
            def factory(self, *args, **kwargs):
                original_result = original(self, *args, **kwargs)
                object.__setattr__(
                    original_result,
                    _ERROR_FIELD,
                    getattr(self, _ERROR_FIELD, False),
                )
                return original_result
        return wraps(original)(factory)


_PatchedContainer = final(_PatchedContainer)

class _DesiredFunctionFound(BaseException):  # noqa: WPS418
    u"""Exception to raise when expected function is found."""
