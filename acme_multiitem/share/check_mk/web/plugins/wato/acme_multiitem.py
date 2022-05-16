#!/usr/bin/env python3

from cmk.gui.i18n import _

from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    TextAscii,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersOperatingSystem,
)


def _item_valuespec_acme_multiitem():
    return TextAscii(title=_("Item name"))


def _parameter_valuespec_acme_multiitem():
    return Dictionary(
        elements=[
            ("levels_lower", Tuple(
                title=_("Levels lower"),
                elements=[
                    Integer(title=_("Warning below"), default_value=0),
                    Integer(title=_("Critical below"), default_value=0),
                ],
            )),
            ("levels_upper", Tuple(
                title=_("Levels upper"),
                elements=[
                    Integer(title=_("Warning at"), default_value=None),
                    Integer(title=_("Critical at"), default_value=None)
                ],
            )),
        ],
    )


def _parameter_valuespec_acme_multiitem_percentage():
    return Dictionary(
        elements=[
            ("levels_lower", Tuple(
                title=_("Levels lower"),
                elements=[
                    Percentage(title=_("Warning below"), default_value=0.0),
                    Percentage(title=_("Critical below"), default_value=0.0),
                ],
            )),
            ("levels_upper", Tuple(
                title=_("Levels upper"),
                elements=[
                    Percentage(title=_("Warning at"), default_value=80.0),
                    Percentage(title=_("Critical at"), default_value=85.0)
                ],
            )),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="acme_multiitem",
        group=RulespecGroupCheckParametersOperatingSystem,
        match_type="dict",
        item_spec=_item_valuespec_acme_multiitem,
        parameter_valuespec=_parameter_valuespec_acme_multiitem,
        title=lambda: _("Acme Multi Items"),
    ))


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="acme_multiitem_percentage",
        group=RulespecGroupCheckParametersOperatingSystem,
        match_type="dict",
        item_spec=_item_valuespec_acme_multiitem,
        parameter_valuespec=_parameter_valuespec_acme_multiitem_percentage,
        title=lambda: _("Acme Multi Items Percentage"),
    ))
