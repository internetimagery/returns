from __future__ import absolute_import
from returns.context import (
    Reader,
    ReaderFutureResult,
    ReaderIOResult,
    ReaderResult,
)
from returns.contrib.hypothesis.laws import check_all_laws
from returns.future import Future, FutureResult
from returns.io import IO, IOResult
from returns.maybe import Maybe
from returns.result import Result

check_all_laws(Maybe)
check_all_laws(Result)

check_all_laws(IO)
check_all_laws(IOResult)

check_all_laws(Future)
check_all_laws(FutureResult)

check_all_laws(Reader)
check_all_laws(ReaderResult)
check_all_laws(ReaderIOResult)
check_all_laws(ReaderFutureResult)
