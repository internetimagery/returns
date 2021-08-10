from __future__ import absolute_import
from typing_extensions import Final

# Constant fullnames for typechecking
# ===================================

#: Set of full names of our decorators.
TYPED_DECORATORS: Final = frozenset((
    u'returns.result.safe',
    u'returns.io.impure',
    u'returns.io.impure_safe',
    u'returns.maybe.maybe',
    u'returns.future.future',
    u'returns.future.asyncify',
    u'returns.future.future_safe',
    u'returns.functions.not_',
))

#: Used for typed ``partial`` function.
TYPED_PARTIAL_FUNCTION: Final = u'returns.curry.partial'

#: Used for typed ``curry`` decorator.
TYPED_CURRY_FUNCTION: Final = u'returns.curry.curry'

#: Used for typed ``flow`` call.
TYPED_FLOW_FUNCTION: Final = u'returns._internal.pipeline.flow.flow'

#: Used for typed ``pipe`` call.
TYPED_PIPE_FUNCTION: Final = u'returns._internal.pipeline.pipe.pipe'
TYPED_PIPE_METHOD: Final = u'returns._internal.pipeline.pipe._Pipe.__call__'

#: Used for HKT emulation.
TYPED_KINDN: Final = u'returns.primitives.hkt.KindN'
TYPED_KINDN_ACCESS: Final = u'{0}.'.format(TYPED_KINDN)
TYPED_KIND_DEKIND: Final = u'returns.primitives.hkt.dekind'
TYPED_KIND_KINDED_CALL: Final = u'returns.primitives.hkt.Kinded.__call__'
TYPED_KIND_KINDED_GET: Final = u'returns.primitives.hkt.Kinded.__get__'
