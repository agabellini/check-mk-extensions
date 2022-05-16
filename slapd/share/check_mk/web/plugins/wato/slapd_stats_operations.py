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

def _item_valuespec_slapd_stats_operations():
    return TextAscii(title=_("Instance"))

def _parameter_valuespec_slapd_stats_operations():
    return Dictionary(
        elements=[
            ("Delete", Tuple(
                title=_("Delete"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Bind", Tuple(
                title=_("Bind"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Add", Tuple(
                title=_("Add"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Abandon", Tuple(
                title=_("Abandon"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Extended", Tuple(
                title=_("Extended"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Search", Tuple(
                title=_("Search"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Modify", Tuple(
                title=_("Modify"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Unbind", Tuple(
                title=_("Unbind"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Modrdn", Tuple(
                title=_("Modrdn"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("Compare", Tuple(
                title=_("Compare"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
            ("deviance", Tuple(
                title=_("Max. Deviance"),
                elements=[
                    Integer(title = _("Warning:"),  default_value = 0),
                    Integer(title = _("Critical:"), default_value = 0)
                ],
            )),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="slapd_stats_operations",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        item_spec=_item_valuespec_slapd_stats_operations,
        parameter_valuespec=_parameter_valuespec_slapd_stats_operations,
        title=lambda: _("slapd Operations"),
    ))
