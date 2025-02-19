from __future__ import absolute_import
from typing import List, Mapping, Optional, Tuple, cast

from mypy.argmap import map_actuals_to_formals
from mypy.constraints import infer_constraints_for_callable
from mypy.expandtype import expand_type
from mypy.nodes import ARG_POS
from mypy.plugin import FunctionContext
from mypy.types import CallableType, FunctionLike
from mypy.types import Type as MypyType
from mypy.types import TypeVarId
from typing_extensions import final

from returns.contrib.mypy._structures.args import FuncArg
from returns.contrib.mypy._structures.types import CallableContext
from returns.contrib.mypy._typeops.analtype import analyze_call
from itertools import izip

#: Mapping of `typevar` to real type.
_Constraints = Mapping[TypeVarId, MypyType]


class CallableInference(object):
    u"""
    Used to infer function arguments and return type.

    There are multiple ways to do it.
    For example, one can infer argument types from its usage.
    """

    def __init__(
        self,
        case_function,
        ctx, **_3to2kwargs
    ):
        if 'fallback' in _3to2kwargs: fallback = _3to2kwargs['fallback']; del _3to2kwargs['fallback']
        else: fallback =  None
        u"""
        Create the callable inference.

        Sometimes we need two functions.
        When construction one function from another
        there might be some lost information during the process.
        That's why we optionally need ``fallback``.
        If it is not provided, we treat ``case_function`` as a full one.

        Args:
            case_function: function with solved constraints.
            fallback: Function with unsolved constraints.
            ctx: Function context with checker and expr_checker objects.

        """
        self._case_function = case_function
        self._fallback = fallback if fallback else self._case_function
        self._ctx = ctx

    def from_usage(
        self,
        applied_args,
    ):
        u"""Infers function constrains from its usage: passed arguments."""
        constraints = self._infer_constraints(applied_args)
        inferred = expand_type(self._case_function, constraints)
        return cast(CallableType, inferred)

    def _infer_constraints(
        self,
        applied_args,
    ):
        u"""Creates mapping of ``typevar`` to real type that we already know."""
        checker = self._ctx.api.expr_checker  # type: ignore
        kinds = [arg.kind for arg in applied_args]
        exprs = [
            arg.expression(self._ctx.context)
            for arg in applied_args
        ]

        formal_to_actual = map_actuals_to_formals(
            kinds,
            [arg.name for arg in applied_args],
            self._fallback.arg_kinds,
            self._fallback.arg_names,
            lambda index: checker.accept(exprs[index]),  # type: ignore
        )
        constraints = infer_constraints_for_callable(
            self._fallback,
            [arg.type for arg in applied_args],
            kinds,
            formal_to_actual,
        )
        return dict((
            constraint.type_var, constraint.target)
            for constraint in constraints)


CallableInference = final(CallableInference)

class PipelineInference(object):
    u"""
    Very helpful tool to work with functions like ``flow`` and ``pipe``.

    It iterates all over the given list of pipeline steps,
    passes the first argument, and then infers types step by step.
    """

    def __init__(self, instance):
        u"""We do need the first argument to start the inference."""
        self._instance = instance

    def from_callable_sequence(
        self,
        pipeline_types,
        pipeline_kinds,
        ctx,
    ):
        u"""Pass pipeline functions to infer them one by one."""
        parameter = FuncArg(None, self._instance, ARG_POS)
        ret_type = ctx.default_return_type

        for pipeline, kind in izip(pipeline_types, pipeline_kinds):
            ret_type = self._proper_type(
                analyze_call(
                    cast(FunctionLike, pipeline),
                    [parameter],
                    ctx,
                    show_errors=True,
                ),
            )
            parameter = FuncArg(None, ret_type, kind)
        return ret_type

    def _proper_type(self, typ):
        if isinstance(typ, CallableType):
            return typ.ret_type
        return typ  # It might be `Instance` or `AnyType` or `Nothing`

PipelineInference = final(PipelineInference)
