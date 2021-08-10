from returns.context import RequiresContextFutureResult as RequiresContextFutureResult
from returns.primitives.hkt import Kind3 as Kind3
from returns.result import Result as Result
from typing import Awaitable, Callable

async def async_bind_async(function: Callable[[_ValueType], Awaitable[Kind3[RequiresContextFutureResult, _NewValueType, _ErrorType, _EnvType]]], container: RequiresContextFutureResult[_ValueType, _ErrorType, _EnvType], deps: _EnvType) -> Result[_NewValueType, _ErrorType]: ...
async def async_compose_result(function: Callable[[Result[_ValueType, _ErrorType]], Kind3[RequiresContextFutureResult, _NewValueType, _ErrorType, _EnvType]], container: RequiresContextFutureResult[_ValueType, _ErrorType, _EnvType], deps: _EnvType) -> Result[_NewValueType, _ErrorType]: ...
