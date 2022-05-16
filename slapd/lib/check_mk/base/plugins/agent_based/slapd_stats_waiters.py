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
# <<<slapd_stats_waiters:sep(44)>>>
# ldap-master02,Write,0
# ldap-master02,Read,2

from .agent_based_api.v1 import *


def parse_slapd_stats_waiters(string_table):
    return string_table


def discover_slapd_stats_waiters(section):
    for name, _op, _value in section:
      yield Service(item=name)


def check_slapd_stats_waiters(item, params, section):
    for name, _op, _value in section:
      if item == name:
        _value = int(_value)
        warn, crit = params[_op]

        yield from check_levels(
          _value,
          levels_upper=(warn, crit),
          metric_name="slapd_waiters_%s" % _op.lower(),
          render_func=lambda v: "%d" % v,
          label="%s Waiters" % _op,
          boundaries=(0, None),
        )

    return


register.check_plugin(
    name="slapd_stats_waiters",
    service_name="SLAPD %s Waiters",
    discovery_function=discover_slapd_stats_waiters,
    check_function=check_slapd_stats_waiters,
    check_default_parameters = {
      "Write": (None, None),
      "Read": (None, None),
    },
    check_ruleset_name="slapd_stats_waiters"
)


register.agent_section(
    name = "slapd_stats_waiters",
    parse_function = parse_slapd_stats_waiters,
)
