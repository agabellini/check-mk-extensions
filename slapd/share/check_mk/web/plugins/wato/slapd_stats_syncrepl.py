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

def _item_valuespec_slapd_syncrepl():
    return TextAscii(title=_("Instance"))

def _parameter_valuespec_slapd_syncrepl():
    return Dictionary(
        elements=[
            ("levels", Tuple(
                title=_("Delta in Change Sequence Number (CSN)"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 10),
                    Integer(title = _("Critical:"), default_value = 20)
                ],
            )),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_syncrepl",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        item_spec=_item_valuespec_slapd_syncrepl,
        parameter_valuespec=_parameter_valuespec_slapd_syncrepl,
        title=lambda: _("slapd Syncrepl status"),
    ))
