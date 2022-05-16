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
# <<<slapd_syncrepl:sep(44)>>>
# ldap-master02,ldap-master01,0.00
# ldap-master02,ldap-master03,0.00

from .agent_based_api.v1 import *


def parse_slapd_syncrepl(string_table):
    return string_table


def discover_slapd_syncrepl(section):
    for name, _master, _value in section:
      yield Service(item=name)


def check_slapd_syncrepl(item, params, section):
    for name, _master, _value in section:
      if item == name:

        if "ERROR" in _value:
          yield Result(state=State.CRIT, summary=_value)
          return

        _value = int(float(_value))
        warn, crit = params["levels"]

        yield Result(
          state=(
            State.CRIT if _value >= crit else
            State.WARN if _value >= warn else
            State.OK),
          summary=("%s" % "Directory %s in sync with Provider %s" % ("not" if _value >= warn else "", _value)),
        )

    return


register.check_plugin(
    name="slapd_syncrepl",
    service_name="SLAPD %s syncrepl status",
    discovery_function=discover_slapd_syncrepl,
    check_function=check_slapd_syncrepl,
    check_default_parameters = {
      'levels': (10, 20)
    },
    check_ruleset_name="slapd_syncrepl"
)


register.agent_section(
    name = "slapd_syncrepl",
    parse_function = parse_slapd_syncrepl,
)
