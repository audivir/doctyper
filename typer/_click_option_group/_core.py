from collections.abc import Mapping, Sequence
from typing import Any

from .._click.core import Context, augment_usage_errors
from .._click.exceptions import UsageError
from ..core import TyperOption


class GroupedOption(TyperOption):
    """Represents grouped (related) optional values

    The class should be used only with `OptionGroup` class for creating grouped options.

    :param param_decls: option declaration tuple
    :param group: `OptionGroup` instance (the group for this option)
    :param attrs: additional option attributes
    """

    def __init__(
        self,
        param_decls: Sequence[str] | None = None,
        *,
        group: "OptionGroup",
        **attrs: Any,
    ):
        super().__init__(param_decls=list(param_decls or []), **attrs)

        for attr in group.forbidden_option_attrs:
            if attrs.get(attr):
                msg = f"'{attr}' attribute is not allowed for '{type(group).__name__}' option `{self.name}'."
                raise TypeError(msg)

        self.__group = group
        group.add_option(self)

    @property
    def group(self) -> "OptionGroup":
        """Returns the reference to the group for this option

        :return: `OptionGroup` the group instance for this option
        """
        return self.__group

    def handle_parse_result(
        self,
        ctx: Context,
        opts: Mapping[str, Any],
        args: list[str],
    ) -> tuple[Any, list[str]]:
        with augment_usage_errors(ctx, param=self):
            if not ctx.resilient_parsing:
                self.group.handle_parse_result(self, ctx, opts)
        return super().handle_parse_result(ctx, opts, args)


class OptionGroup:
    """Option group manages grouped (related) options

    The class is used for creating the groups of options. The class can de used as based class to implement
    specific behavior for grouped options.

    :param name: the group name
    """

    def __init__(self, name: str) -> None:
        self._name = name
        self._options: dict[str, GroupedOption] = {}

    @property
    def name(self) -> str:
        """Returns the group name

        :return: group name
        """
        return self._name

    @property
    def forbidden_option_attrs(self) -> list[str]:
        """Returns the list of forbidden option attributes for the group"""
        return []

    def add_option(self, option: GroupedOption) -> None:
        """Adds an option to the group"""
        assert option.name is not None
        self._options[option.name] = option

    def get_options(self) -> dict[str, GroupedOption]:
        """Returns the dictionary with group options ordered by addition"""
        return self._options

    def get_error_hint(self, ctx: Context, option_names: set[str]) -> str:
        return "\n".join(
            f"  {opt.get_error_hint(ctx)}"
            for name, opt in self.get_options().items()
            if name in option_names
        )

    def handle_parse_result(
        self, option: GroupedOption, ctx: Context, opts: Mapping[str, Any]
    ) -> None:
        """The method should be used for adding specific behavior and relation for options in the group"""


class MutuallyExclusiveOptionGroup(OptionGroup):
    """Option group with mutually exclusive behavior for grouped options

    `MutuallyExclusiveOptionGroup` defines the behavior:
        - Only one or none option from the group must be set
    """

    @property
    def forbidden_option_attrs(self) -> list[str]:
        return ["required"]

    def handle_parse_result(
        self, option: GroupedOption, ctx: Context, opts: Mapping[str, Any]
    ) -> None:
        option_names = set(self.get_options())
        given_option_names = option_names.intersection(opts)

        if len(given_option_names) > 1:
            option_info = self.get_error_hint(ctx, given_option_names)

            msg = f"Mutually exclusive options from '{self.name}' option group cannot be used at the same time:\n{option_info}"
            raise UsageError(msg, ctx=ctx)
