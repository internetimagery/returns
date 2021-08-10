from __future__ import absolute_import
def assert_equal(
    first,
    second, **_3to2kwargs
):
    if 'backend' in _3to2kwargs: backend = _3to2kwargs['backend']; del _3to2kwargs['backend']
    else: backend =  u'asyncio'
    if 'deps' in _3to2kwargs: deps = _3to2kwargs['deps']; del _3to2kwargs['deps']
    else: deps = None
    u"""
    Custom ``assert`` function to compare two any containers.

    The important note here is that
    this ``assert`` should probably used in tests.
    Not real application code.

    It will call all ``Reader`` based containers and ``await``
    all ``Future`` based ones.

    It also works recursively.
    For example, ``ReaderFutureResult`` will be called and then awaited.

    You can specify different dependencies to call your containers.
    And different backends to ``await`` then using ``anyio``.

    By the way, ``anyio`` should be installed separately.
    """
    assert _convert(
        first, deps=deps, backend=backend,
    ) == _convert(
        second, deps=deps, backend=backend,
    ), u'{0} == {1}'.format(first, second)


def _convert(container, **_3to2kwargs):
    backend = _3to2kwargs['backend']; del _3to2kwargs['backend']
    deps = _3to2kwargs['deps']; del _3to2kwargs['deps']
    from returns.interfaces.specific import future, reader

    if isinstance(container, future.AwaitableFutureN):
        import anyio

        return _convert(
            anyio.run(container.awaitable, backend=backend),
            deps=deps,
            backend=backend,
        )
    elif isinstance(container, reader.Contextable):
        return _convert(
            container(deps),
            deps=deps,
            backend=backend,
        )
    return container
