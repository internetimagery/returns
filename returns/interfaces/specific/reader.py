u"""
This module is special.

``Reader`` does not produce ``ReaderLikeN`` interface as other containers.

Because ``Reader`` can be used with two or three type arguments:
- ``RequiresContext[value, env]``
- ``RequiresContextResult[value, error, env]``

Because the second type argument changes its meaning
based on the used ``KindN`` instance,
we need to have two separate interfaces for two separate use-cases:
- ``ReaderLike2`` is used for types where the second type argument is ``env``
- ``ReaderLike3`` is used for types where the third type argument is ``env``

We also have two methods and two poinfree helpers
for ``bind_context`` composition: one for each interface.

Furthermore, ``Reader`` cannot have ``ReaderLike1`` type,
because we need both ``value`` and ``env`` types at all cases.

See also:
    - https://github.com/dry-python/returns/issues/485

"""

from __future__ import absolute_import

from abc import abstractmethod
from typing import (
    TYPE_CHECKING,
    Callable,
    ClassVar,
    Generic,
    Sequence,
    Type,
    TypeVar,
)

from returns.interfaces.container import Container2, Container3
from returns.primitives.hkt import Kind2, Kind3
from returns.primitives.laws import (
    Law,
    Law2,
    Lawful,
    LawSpecDef,
    law_definition,
)

if TYPE_CHECKING:
    from returns.context import NoDeps, RequiresContext  # noqa: WPS433

_FirstType = TypeVar(u'_FirstType')
_SecondType = TypeVar(u'_SecondType')
_ThirdType = TypeVar(u'_ThirdType')
_UpdatedType = TypeVar(u'_UpdatedType')

_ValueType = TypeVar(u'_ValueType')
_ErrorType = TypeVar(u'_ErrorType')
_EnvType = TypeVar(u'_EnvType')

_ReaderLike2Type = TypeVar(u'_ReaderLike2Type', bound=u'ReaderLike2')
_ReaderLike3Type = TypeVar(u'_ReaderLike3Type', bound=u'ReaderLike3')


class Contextable(Generic[_ValueType, _EnvType]):
    u"""
    Special type we use as a base one for all callble ``Reader`` instances.

    It only has a single method.
    And is a base type for every single one of them.

    But, each ``Reader`` defines the return type differently.
    For example:

    - ``Reader`` has just ``_ReturnType``
    - ``ReaderResult`` has ``Result[_FirstType, _SecondType]``
    - ``ReaderIOResult`` has ``IOResult[_FirstType, _SecondType]``

    And so on.
    """

    @abstractmethod
    def __call__(self, deps):
        u"""Receives one parameter, returns a value. As simple as that."""


class ReaderLike2(Container2[_FirstType, _SecondType]):
    u"""
    Reader interface for ``Kind2`` based types.

    It has two type arguments and treats the second type argument as env type.
    """

    @property
    @abstractmethod
    def no_args(self):
        u"""Is required to call ``Reader`` with no explicit arguments."""

    @abstractmethod
    def bind_context(
        self,
        function,
    ):
        u"""Allows to apply a wrapped function over a ``Reader`` container."""

    @abstractmethod
    def modify_env(
        self,
        function,
    ):
        u"""Transforms the environment before calling the container."""

    @classmethod
    @abstractmethod
    def ask(
        cls,
    ):
        u"""Returns the dependencies inside the container."""

    @classmethod
    @abstractmethod
    def from_context(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Unit method to create new containers from successful ``Reader``."""


class CallableReader2(
    ReaderLike2[_FirstType, _SecondType],
    Contextable[_ValueType, _EnvType],
):
    u"""
    Intermediate interface for ``ReaderLike2`` + ``__call__`` method.

    Has 4 type variables to type ``Reader`` and ``__call__`` independently.
    Since, we don't have any other fancy ways of doing it.

    Should not be used directly
    other than defining your own ``Reader`` interfaces.
    """


class ReaderLike3(Container3[_FirstType, _SecondType, _ThirdType]):
    u"""
    Reader interface for ``Kind3`` based types.

    It has three type arguments and treats the third type argument as env type.
    The second type argument is not used here.
    """

    @property
    @abstractmethod
    def no_args(self):
        u"""Is required to call ``Reader`` with no explicit arguments."""

    @abstractmethod
    def bind_context(
        self,
        function,
    ):
        u"""Allows to apply a wrapped function over a ``Reader`` container."""

    @abstractmethod
    def modify_env(
        self,
        function,
    ):
        u"""Transforms the environment before calling the container."""

    @classmethod
    @abstractmethod
    def ask(
        cls,
    ):
        u"""Returns the dependencies inside the container."""

    @classmethod
    @abstractmethod
    def from_context(
        cls,  # noqa: N805
        inner_value,
    ):
        u"""Unit method to create new containers from successful ``Reader``."""


class CallableReader3(
    ReaderLike3[_FirstType, _SecondType, _ThirdType],
    Contextable[_ValueType, _EnvType],
):
    u"""
    Intermediate interface for ``ReaderLike3`` + ``__call__`` method.

    Has 5 type variables to type ``Reader`` and ``__call__`` independently.
    Since, we don't have any other fancy ways of doing it.

    Should not be used directly
    other than defining your own ``Reader`` interfaces.
    """


class _LawSpec(LawSpecDef):
    u"""
    Concrete laws for ``ReaderBased2``.

    See: https://github.com/haskell/mtl/pull/61/files
    """

    @law_definition
    def purity_law(
        container,
        env,
    ):
        u"""Calling a ``Reader`` twice has the same result with the same env."""
        assert container(env) == container(env)

    @law_definition
    def asking_law(
        container,
        env,
    ):
        u"""Asking for an env, always returns the env."""
        assert container.ask().__call__(    # noqa: WPS609
            env,
        ) == container.from_value(env).__call__(env)  # noqa: WPS609


class ReaderBased2(
    CallableReader2[
        _FirstType,
        _SecondType,
        # Used for call typing:
        _FirstType,
        _SecondType,
    ],
    Lawful[u'ReaderBased2[_FirstType, _SecondType]'],
):
    u"""
    This interface is very specific to our ``Reader`` type.

    The only thing that differs from ``ReaderLike2`` is that we know
    the specific types for its ``__call__`` method.
    """

    _laws = (
        Law2(_LawSpec.purity_law),
        Law2(_LawSpec.asking_law),
    ) # type: ClassVar[Sequence[Law]]
