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
# <<<slapd_instance:sep(124)>>>
# ldap-slave1|0.0000
# <<<slapd_instance:sep(124)>>>
# ldap-slave2|ERROR - could not bind as cn=Monitor : Invalid credentials at ./slapd.pl line 344
#  at ./slapd.pl line 344

from .agent_based_api.v1 import *

def parse_slapd_instance(string_table):
    return string_table


def discover_slapd_instance(section):
    for name, _value in section:
      yield Service(item=name)


def check_slapd_instance(item, params, section):
    for name, _value in section:
      if item == name:
        warn, crit = params["levels_upper"]

        if "ERROR" in _value:
          yield Result(state=State.CRIT, summary=_value)
          return

        yield from check_levels(
          float(_value),
          levels_upper=(warn, crit),
          metric_name="connection_time",
          render_func=lambda v: "%s" % render.timespan(v),
          label="Connected in",
          boundaries=(0, None),
        )

    return


register.check_plugin(
    name="slapd_instance",
    service_name="SLAPD %s",
    discovery_function=discover_slapd_instance,
    check_function=check_slapd_instance,
    check_default_parameters = { 'levels_upper': (None, None) },
    check_ruleset_name="slapd_instance"
)


register.agent_section(
    name = "slapd_instance",
    parse_function = parse_slapd_instance,
)
