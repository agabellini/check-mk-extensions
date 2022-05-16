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
    RulespecGroupCheckParametersApplications,
)

def _item_valuespec_slapd_stats_waiters():
    return TextAscii(title=_("Instance"))

def _parameter_valuespec_slapd_stats_waiters():
    return Dictionary(
        elements=[
            ("Write", Tuple(
                title=_("Write Waiters"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Read", Tuple(
                title=_("Read Waiters"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_stats_waiters",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        item_spec=_item_valuespec_slapd_stats_waiters,
        parameter_valuespec=_parameter_valuespec_slapd_stats_waiters,
        title=lambda: _("slapd Waiters"),
    ))
