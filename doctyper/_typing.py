# Copied from pydantic 1.9.2 (the latest version to support python 3.6.)
# https://github.com/pydantic/pydantic/blob/v1.9.2/pydantic/typing.py
# Reduced drastically to only include Typer-specific 3.7+ functionality
# mypy: ignore-errors

import sys
import types
from typing import (
    Any,
    Callable,
    Dict,
    ForwardRef,
    Mapping,
    Optional,
    Tuple,
    Type,
    Union,
)

if sys.version_info >= (3, 9):
    from typing import (
        Annotated,
        Literal,
        get_args,
        get_origin,
    )
else:
    from typing_extensions import (
        Annotated,
        Literal,
        get_args,
        get_origin,
    )

if sys.version_info >= (3, 9):
    from typing import _strip_annotations
else:
    from typing_extensions import _strip_extras as _strip_annotations

if sys.version_info < (3, 10):

    def is_union(tp: Optional[Type[Any]]) -> bool:
        return tp is Union

else:
    import types

    def is_union(tp: Optional[Type[Any]]) -> bool:
        return tp is Union or tp is types.UnionType  # noqa: E721


# from python version 3.13 on a DeprecationWarning is raised
# if no type_params are passed to _eval_type, so we need to pass an empty tuple
# as we don't need eval_type_backport anymore
if sys.version_info < (3, 13):
    from eval_type_backport import eval_type_backport as eval_type

else:
    from typing import _eval_type

    def eval_type(
        value: Any,
        globalns: Optional[Dict[str, Any]] = None,
        localns: Optional[Mapping[str, Any]] = None,
        try_default: bool = True,
    ) -> Type[Any]:
        del try_default  # Unused.
        return _eval_type(value, globalns, localns, type_params=())


__all__ = (
    "NoneType",
    "is_none_type",
    "is_callable_type",
    "is_literal_type",
    "all_literal_values",
    "is_union",
    "Annotated",
    "Literal",
    "get_args",
    "get_origin",
    "get_type_hints",
    "is_type_alias_type",
    "is_annotated_type",
    "eval_type",
)


NoneType = None.__class__


NONE_TYPES: Tuple[Any, Any, Any] = (None, NoneType, Literal[None])


if sys.version_info < (3, 8):
    # Even though this implementation is slower, we need it for python 3.7:
    # In python 3.7 "Literal" is not a builtin type and uses a different
    # mechanism.
    # for this reason `Literal[None] is Literal[None]` evaluates to `False`,
    # breaking the faster implementation used for the other python versions.

    def is_none_type(type_: Any) -> bool:
        return type_ in NONE_TYPES

elif sys.version_info[:2] == (3, 8):
    # We can use the fast implementation for 3.8 but there is a very weird bug
    # where it can fail for `Literal[None]`.
    # We just need to redefine a useless `Literal[None]` inside the function body to fix this

    def is_none_type(type_: Any) -> bool:
        Literal[None]  # fix edge case
        for none_type in NONE_TYPES:
            if type_ is none_type:
                return True
        return False

else:

    def is_none_type(type_: Any) -> bool:
        for none_type in NONE_TYPES:
            if type_ is none_type:
                return True
        return False


def is_callable_type(type_: Type[Any]) -> bool:
    return type_ is Callable or get_origin(type_) is Callable


def is_literal_type(type_: Type[Any]) -> bool:
    from typing_extensions import Literal as _ExtLiteral

    if get_origin(type_) is _ExtLiteral:
        return True
    if sys.version_info >= (3, 8):
        from typing import Literal as _Literal

        return get_origin(type_) is _Literal
    return False


def literal_values(type_: Type[Any]) -> Tuple[Any, ...]:
    return get_args(type_)


def all_literal_values(type_: Type[Any]) -> Tuple[Any, ...]:
    """
    This method is used to retrieve all Literal values as
    Literal can be used recursively (see https://www.python.org/dev/peps/pep-0586)
    e.g. `Literal[Literal[Literal[1, 2, 3], "foo"], 5, None]`
    """
    if not is_literal_type(type_):
        return (type_,)

    values = literal_values(type_)
    return tuple(x for value in values for x in all_literal_values(value))


def is_annotated_type(type_: Type[Any]) -> bool:
    from typing_extensions import Annotated as _ExtAnnotated

    if type_ is _ExtAnnotated:
        return True
    if sys.version_info >= (3, 9):
        from typing import Annotated as _Annotated

        if type_ is _Annotated:
            return True
    return False


def is_type_alias_type(type_: Type[Any]) -> bool:
    from typing_extensions import TypeAliasType as _ExtTypeAliasType

    if type_ is _ExtTypeAliasType:
        return True
    if sys.version_info >= (3, 12):
        from typing import TypeAliasType as _TypeAliasType

        if type_ is _TypeAliasType:
            return True
    return False


def get_type_hints(
    obj: Callable[..., Any],
    globalns: Any = None,
    localns: Any = None,
    include_extras: bool = False,
) -> Dict[str, Any]:
    """Return type hints for an object.

    This is often the same as obj.__annotations__, but it handles
    forward references encoded as string literals and recursively replaces all
    'Annotated[T, ...]' with 'T' (unless 'include_extras=True').

    The argument may be a module, class, method, or function. The annotations
    are returned as a dictionary. For classes, annotations include also
    inherited members.

    TypeError is raised if the argument is not of a type that can contain
    annotations, and an empty dictionary is returned if no annotations are
    present.

    BEWARE -- the behavior of globalns and localns is counterintuitive
    (unless you are familiar with how eval() and exec() work).  The
    search order is locals first, then globals.

    - If no dict arguments are passed, an attempt is made to use the
      globals from obj (or the respective module's globals for classes),
      and these are also used as the locals.  If the object does not appear
      to have globals, an empty dictionary is used.  For classes, the search
      order is globals first then locals.

    - If one dict argument is passed, it is used for both globals and
      locals.

    - If two dict arguments are passed, they specify globals and
      locals, respectively.
    """
    if getattr(obj, "__no_type_check__", None):
        return {}
    # We don't need class evaluations for analyzing commands.
    # shortens the copied function body a bit.
    if isinstance(obj, type):
        raise TypeError("Class annotations are not supported.")

    if globalns is None:
        if isinstance(obj, types.ModuleType):
            globalns = obj.__dict__
        else:
            nsobj = obj
            # Find globalns for the unwrapped object.
            while hasattr(nsobj, "__wrapped__"):
                nsobj = nsobj.__wrapped__
            globalns = getattr(nsobj, "__globals__", {})
        if localns is None:
            localns = globalns
    elif localns is None:
        localns = globalns
    hints = getattr(obj, "__annotations__", None)
    if hints is None:
        # Return empty annotations for something that _could_ have them.
        if isinstance(
            obj,
            (
                types.FunctionType,
                types.MethodType,
                types.BuiltinFunctionType,
                types.MethodWrapperType,
            ),
        ):
            return {}
        else:
            raise TypeError(
                "{!r} is not a module, class, method, or function.".format(obj)  # noqa: UP032
            )
    hints = dict(hints)
    type_params = getattr(obj, "__type_params__", ())
    # TypeVarTuple etc. not yet supported
    if type_params:
        raise TypeError("Type parameters are not yet supported.")
    for name, value in hints.items():
        if value is None:
            value = type(None)
        if isinstance(value, str):
            # class-level forward refs were handled above, this must be either
            # a module-level annotation or a function argument annotation
            value = ForwardRef(
                value,
                is_argument=not isinstance(obj, types.ModuleType),
                # is_class is False per default and not available in Python 3.8
            )
        if is_annotated_type(get_origin(value)):
            # Annotated[ForwardRef(...), ...] is evaluated wrongly by eval_type_backport,
            # so we evaluate the forward ref first and then the annotation
            args = list(get_args(value))
            args[0] = eval_type(args[0], globalns, localns)
            value = type(Annotated[int, "placeholder"])(args[0], tuple(args[1:]))

        hints[name] = eval_type(value, globalns, localns)
    return (
        hints
        if include_extras
        else {k: _strip_annotations(t) for k, t in hints.items()}
    )
