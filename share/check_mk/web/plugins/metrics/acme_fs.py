#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: GNU General Public License v2

from cmk.gui.plugins.metrics import check_metrics
from cmk.gui.plugins.metrics.translation import df_translation

check_metrics["check_mk-acme_fs"] = df_translation
