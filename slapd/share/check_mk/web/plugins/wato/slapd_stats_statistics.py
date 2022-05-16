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

def _item_valuespec_slapd_stats_statistics():
    return TextAscii(title=_("Instance"))

def _parameter_valuespec_slapd_stats_statistics():
    return Dictionary(
        elements=[
            ("Entries", Tuple(
                title=_("Entries rate"),
                elements=[
                    Float(title = _("Warning:"),  default_value = 0.0),
                    Float(title = _("Critical:"), default_value = 0.0)
                ],
            )),
            ("Referrals", Tuple(
                title=_("Referrals rate"),
                elements=[
                    Float(title = _("Warning:"),  default_value = 0.0),
                    Float(title = _("Critical:"), default_value = 0.0)
                ],
            )),
            ("PDU", Tuple(
                title=_("PDU rate"),
                elements=[
                    Float(title = _("Warning:"),  default_value = 0.0),
                    Float(title = _("Critical:"), default_value = 0.0)
                ],
            )),
            ("Bytes", Tuple(
                title=_("Bytes rate"),
                elements=[
                    Float(title = _("Warning:"),  default_value = 0.0),
                    Float(title = _("Critical:"), default_value = 0.0)
                ],
            )),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_stats_statistics",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        item_spec=_item_valuespec_slapd_stats_statistics,
        parameter_valuespec=_parameter_valuespec_slapd_stats_statistics,
        title=lambda: _("slapd Network Statistics"),
    ))
