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
from .agent_based_api.v1 import *


def discover_cisco_ip_pool(section):
    for name, used, free in section:
      yield Service(item=name)


def parse_cisco_ip_pool(string_table):
    parsed = []
    for line in string_table:
      for elem in line:
        parsed.append(elem)

    return parsed


def check_cisco_ip_pool(item, params, section):
    for name, used, free in section:
      if name == item:
        warn, crit = params["levels_upper"]
        used = int(used)
        free = int(free)
        used_perc = (used / (used + free)) * 100

        yield from check_levels(
          used_perc,
          levels_upper=(warn, crit),
          metric_name="ip_pool_used_perc",
          render_func=lambda v: "%.2f%%" % v,
          label="Used",
          boundaries=(0, 100),
        )

        yield from check_levels(
          free,
          #levels_lower=(warn, crit),
          metric_name="ip_pool_free",
          render_func=lambda v: "%d" % v,
          label="Free",
          boundaries=(0, None),
        )

        return


register.check_plugin(
    name="cisco_ip_pool",
    service_name="Cisco IP Pool %s",
    discovery_function=discover_cisco_ip_pool,
    check_function=check_cisco_ip_pool,
    check_default_parameters = {
      'levels_upper': (85.0, 90.0),
    },
    check_ruleset_name="cisco_ip_pool",
)

register.snmp_section(
    name = "cisco_ip_pool",
    parse_function=parse_cisco_ip_pool,
    detect = any_of(
      exists(".1.3.6.1.4.1.9.9.326.1.2.2.1.1.0"), # Cisco IOS
      exists(".1.3.6.1.4.1.9.9.748.1.2.2.1.2.0"), # Cisco IOS XR
    ),
    fetch = [
      SNMPTree(
        base = '.1.3.6.1.4.1.9.9.326.1',
        oids = [
          '2.1.1.2.0', # Pool Name
          '3.1.1.2',   # Pool Used
          '3.1.1.1',   # Pool Free
        ],
      ),
      SNMPTree(
      base = '.1.3.6.1.4.1.9.9.748.1.2.2.1',
      oids = [
        '4',      # Pool Name
        '10',     # Pool Used
        '11',     # Pool Free
      ],
    ),
  ],
)
