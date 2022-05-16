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

def _item_valuespec_cisco_ip_pool():
    return TextAscii(title=_("Pool name"))

def _parameter_valuespec_cisco_ip_pool():
    return Dictionary(
        elements=[
            #("levels_lower", Tuple(
            #    title=_("Levels on free IP"),
            #    elements=[
            #        Integer(title=_("Warning below"), default_value=15),
            #        Integer(title=_("Critical below"), default_value=5),
            #    ],
            #)),
            ("levels_upper", Tuple(
                title=_("Levels on used IP"),
                elements=[
                    Percentage(title=_("Warning at"), default_value=85.0),
                    Percentage(title=_("Critical at"), default_value=90.0)
                ],
            )),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="cisco_ip_pool",
        group=RulespecGroupCheckParametersOperatingSystem,
        match_type="dict",
        item_spec=_item_valuespec_cisco_ip_pool,
        parameter_valuespec=_parameter_valuespec_cisco_ip_pool,
        title=lambda: _("Free IP for Cisco IP Pool"),
    ))
