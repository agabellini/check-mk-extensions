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
# <<<slapd_stats_connections:sep(44)>>>
# ldap-slave1,Total,8555
# ldap-slave1,Current,16

from .agent_based_api.v1 import *
import time


map_metric = {
  'Total':   'connections',
  'Current': 'active'
}


def parse_slapd_stats_connections(string_table):
    return string_table


def discover_slapd_stats_connections(section):
    for name, _op, _value in section:
      yield Service(item=name)


def check_slapd_stats_connections(item, params, section):
    for name, _op, _value in section:
      if item == name:
        _value = int(_value)
        warn, crit = params[_op]

        if _op == "Total":
          this_time = int(time.time())
          value_store = get_value_store()
          warn_r, crit_r = params["Rate"]
          rate = get_rate(value_store, "slapd.stats.connections.%s" % _op, this_time, _value)

          yield from check_levels(
            float(rate),
            levels_upper=(warn_r, crit_r),
            metric_name="connections_rate",
            render_func=lambda v: "%.2f/s" % v,
            label="Connections rate",
            boundaries=(0, None),
          )

        yield from check_levels(
          _value,
          levels_upper=(warn, crit),
          metric_name=map_metric[_op],
          render_func=lambda v: "%d" % v,
          label="%s connections" % _op,
          boundaries=(0, None),
        )

    return


register.check_plugin(
    name="slapd_stats_connections",
    service_name="SLAPD %s Connections",
    discovery_function=discover_slapd_stats_connections,
    check_function=check_slapd_stats_connections,
    check_default_parameters = {
      "Current": (None, None),
      "Rate":    (None, None),
      "Total":   (None, None),
    },
    check_ruleset_name="slapd_stats_connections"
)


register.agent_section(
    name = "slapd_stats_connections",
    parse_function = parse_slapd_stats_connections,
)
