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

def _item_valuespec_slapd_stats_connections():
    return TextAscii(title=_("Instance"))

def _parameter_valuespec_slapd_stats_connections():
    return Dictionary(
        elements=[
            ("Current", Tuple(
                title=_("Current Connections"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Total", Tuple(
                title=_("Total Connections"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Rate", Tuple(
                title=_("Connections rate"),
                elements=[
                    Float(title = _("Warning:"),  default_value = 0.0),
                    Float(title = _("Critical:"), default_value = 0.0)
                ],
            )),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_stats_connections",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        item_spec=_item_valuespec_slapd_stats_connections,
        parameter_valuespec=_parameter_valuespec_slapd_stats_connections,
        title=lambda: _("slapd Connections"),
    ))
