#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

# Example Output:
# <<<slapd_stats_operations:sep(44)>>>
# ldap-instance1,Delete,0,0
# ldap-instance1,Bind,82095,82095
# ldap-instance1,Add,0,0
# ldap-instance1,Abandon,0,0
# ldap-instance1,Extended,14978,14978
# ldap-instance1,Search,74380,74379
# ldap-instance1,Modify,0,0
# ldap-instance1,Unbind,16423,16423
# ldap-instance1,Modrdn,0,0
# ldap-instance1,Compare,0,0

from .agent_based_api.v1 import *
import time


def parse_slapd_stats_operations(string_table):
    return string_table


def discover_slapd_stats_operations(section):
    for name, _op, _initiated, _completed in section:
      yield Service(item=name)


def check_slapd_stats_operations(item, params, section):
    for name, _op, _initiated, _completed in section:
      if item == name:
        _initiated = int(_initiated)
        _completed = int(_completed)
        deviance = max(0, abs(_initiated - _completed))
        warn, crit = params[_op]
        warn_dev, crit_dev = params["deviance"]

        this_time = int(time.time())
        value_store = get_value_store()
        rate = get_rate(value_store, "slapd.stats.operations.%s" % _op, this_time, _completed)

        yield from check_levels(
          float(rate),
          levels_upper=(warn, crit),
          metric_name="slapd_%s" % _op.lower(),
          render_func=lambda v: "%.3f/s" % v,
          label="%s rate" % _op,
          boundaries=(0, None),
        )

        yield from check_levels(
          int(deviance),
          levels_upper=(warn_dev, crit_dev),
          metric_name=None,
          render_func=lambda v: "%d" % v,
          label="%s deviance" % _op,
          boundaries=(0, None),
          notice_only=True,
        )

    return


register.check_plugin(
    name="slapd_stats_operations",
    service_name="SLAPD %s Operations",
    discovery_function=discover_slapd_stats_operations,
    check_function=check_slapd_stats_operations,
    check_default_parameters = {
      'deviance': (None, None),
      'Delete': (None, None),
      'Bind': (None, None),
      'Add': (None, None),
      'Abandon': (None, None),
      'Extended': (None, None),
      'Search': (None, None),
      'Modify': (None, None),
      'Unbind': (None, None),
      'Modrdn': (None, None),
      'Compare': (None, None),
    },
    check_ruleset_name="slapd_stats_operations"
)


register.agent_section(
    name = "slapd_stats_operations",
    parse_function = parse_slapd_stats_operations,
)
