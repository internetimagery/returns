from __future__ import absolute_import
from typing import Any, Dict, NoReturn

from returns.primitives.exceptions import ImmutableStateError


class Immutable(object):
    u"""
    Helper type for objects that should be immutable.

    When applied, each instance becomes immutable.
    Nothing can be added or deleted from it.

    .. code:: pycon
      :force:

      >>> from returns.primitives.types import Immutable
      >>> class MyModel(Immutable):
      ...     ...

      >>> model = MyModel()
      >>> model.prop = 1
      Traceback (most recent call last):
         ...
      returns.primitives.exceptions.ImmutableStateError

    See :class:`returns.primitives.container.BaseContainer` for examples.

    """  # noqa: RST307

    def __copy__(self):
        u"""Returns itself."""
        return self

    def __deepcopy__(self, memo):
        u"""Returns itself."""
        return self

    def __setattr__(self, attr_name, attr_value):
        u"""Makes inner state of the containers immutable for modification."""
        raise ImmutableStateError()

    def __delattr__(self, attr_name):  # noqa: WPS603
        u"""Makes inner state of the containers immutable for deletion."""
        raise ImmutableStateError()
