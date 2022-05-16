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

def _item_valuespec_slapd_instance():
    return TextAscii(title=_("Instance"))

def _parameter_valuespec_slapd_instance():
    return Dictionary(
        elements=[
            ("levels_upper", Tuple(
                title=_("Max. response time"),
                elements=[
                    Float(title = _("Warning:"),  default_value = 0.0, unit = _("seconds")),
                    Float(title = _("Critical:"), default_value = 0.0, unit = _("seconds"))
                ],
            )),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_instance",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        item_spec=_item_valuespec_slapd_instance,
        parameter_valuespec=_parameter_valuespec_slapd_instance,
        title=lambda: _("slapd Instance"),
    ))
