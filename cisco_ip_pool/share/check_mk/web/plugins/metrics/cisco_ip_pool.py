#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: GNU General Public License v2
#

from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import metric_info

metric_info["ip_pool_used_perc"] = {
    "title": _("Used IP in Pool"),
    "unit": "%",
    "color": "14/a",
}


metric_info["ip_pool_free"] = {
    "title": _("Free IP in Pool"),
    "unit": "count",
    "color": "14/b",
}
