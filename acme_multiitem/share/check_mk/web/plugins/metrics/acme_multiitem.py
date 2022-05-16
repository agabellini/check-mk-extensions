#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: GNU General Public License v2
#
from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import metric_info


metric_info["acme_cpu_utilization"] = {
    "title": _("CPU Utilization"),
    "unit": "%",
    "color": "32/a",
}

metric_info["acme_memory_utilization"] = {
    "title": _("Memory Utilization"),
    "unit": "%",
    "color": "43/a",
}

metric_info["acme_active_sessions"] = {
    "title": _("Active Sessions"),
    "unit": "count",
    "color": "15/a",
}

metric_info["acme_cached_registrations"] = {
    "title": _("Cached Registrations"),
    "unit": "count",
    "color": "22/a",
}

metric_info["acme_licences"] = {
    "title": _("Licences"),
    "unit": "%",
    "color": "16/a",
}

metric_info["acme_calls_per_second"] = {
    "title": _("Calls per Second"),
    "unit": "count",
    "color": "34/a",
}
