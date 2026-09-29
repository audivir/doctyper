from collections.abc import Mapping, Sequence
from gettext import gettext as _
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

        if attrs.get("required"):
            msg = (
                f"Option '{self.name}' of option group '{group.name}' must not be required: "
                f"give it a default (e.g. None) or use `typer.Mutex('{group.name}', required=True)`."
            )
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

    help_extra = _("option group: {name}")

    def __init__(self, name: str) -> None:
        self._name = name
        self._options: dict[str, GroupedOption] = {}

    @property
    def name(self) -> str:
        """Returns the group name

        :return: group name
        """
        return self._name

    def get_help_extra(self) -> str:
        """Returns the marker shown in the help text of the group options"""
        return self.help_extra.format(name=self.name)

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

    help_extra = _("mutually exclusive: {name}")

    def handle_parse_result(
        self, option: GroupedOption, ctx: Context, opts: Mapping[str, Any]
    ) -> None:
        option_names = set(self.get_options())
        given_option_names = option_names.intersection(opts)

        if len(given_option_names) > 1:
            option_info = self.get_error_hint(ctx, given_option_names)

            msg = f"Mutually exclusive options from '{self.name}' option group cannot be used at the same time:\n{option_info}"
            raise UsageError(msg, ctx=ctx)


class RequiredMutuallyExclusiveOptionGroup(MutuallyExclusiveOptionGroup):
    """Option group with required and mutually exclusive behavior for grouped options

    `RequiredMutuallyExclusiveOptionGroup` defines the behavior:
        - Only one required option from the group must be set
    """

    help_extra = _("exactly one of: {name}")

    def handle_parse_result(
        self, option: GroupedOption, ctx: Context, opts: Mapping[str, Any]
    ) -> None:
        super().handle_parse_result(option, ctx, opts)

        option_names = set(self.get_options())

        if not option_names.intersection(opts):
            option_info = self.get_error_hint(ctx, option_names)

            msg = f"Missing one of the required mutually exclusive options from '{self.name}' option group:\n{option_info}"
            raise UsageError(msg, ctx=ctx)
