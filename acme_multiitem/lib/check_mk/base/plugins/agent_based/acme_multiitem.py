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


map_snmp_to_desc = {
    "1" : {'desc': 'Active Sessions',      'unit': ''  },
    "2" : {'desc': 'Calls per second',     'unit': ''  },
    "3" : {'desc': 'Cached Registrations', 'unit': ''  },
}


map_snmp_to_desc_percentage = {
    "1" : {'desc': 'CPU Utilization',      'unit': '%' },
    "2" : {'desc': 'Memory Utilization',   'unit': '%' },
    "3" : {'desc': 'Licences',             'unit': '%' },
}


def parse_acme_multiitem(string_table):
    parsed = {}
    for line in string_table:
      i=0
      for value in line:
        i += 1
        if value:
          desc = map_snmp_to_desc[str(i)]['desc']
          unit = map_snmp_to_desc[str(i)]['unit']
          parsed[desc] = {}
          parsed[desc]['value'] = int(value)
          parsed[desc]['unit']  = str(unit)

    return parsed


def parse_acme_multiitem_percentage(string_table):
    parsed = {}
    for line in string_table:
      i=0
      for value in line:
        i += 1
        if value:
          desc = map_snmp_to_desc_percentage[str(i)]['desc']
          unit = map_snmp_to_desc_percentage[str(i)]['unit']
          parsed[desc] = {}
          parsed[desc]['value'] = int(value)
          parsed[desc]['unit']  = str(unit)

    return parsed



def discover_acme_multiitem(section):
    for name in section:
      yield Service(item=name)


def check_acme_multiitem(item, params, section):
    if item in section:
      value     = section[item]['value']
      unit      = section[item]['unit']

      warn_low, crit_low = params["levels_lower"]
      warn_up,  crit_up  = params["levels_upper"]

      yield from check_levels(
        value,
        levels_lower=(warn_low, crit_low),
        levels_upper=(warn_up,  crit_up),
        metric_name="acme_%s" % item.replace(' ','_').lower(),
        render_func=lambda v: "%d%s" % (v, unit),
      )

      return


register.check_plugin(
    name="acme_multiitem",
    service_name="%s",
    discovery_function=discover_acme_multiitem,
    check_function=check_acme_multiitem,
    check_default_parameters = {
      'levels_lower': (0, 0),
      'levels_upper': (None, None),
    },
    check_ruleset_name="acme_multiitem",
)

register.check_plugin(
    name="acme_multiitem_percentage",
    service_name="%s",
    discovery_function=discover_acme_multiitem,
    check_function=check_acme_multiitem,
    check_default_parameters = {
      'levels_lower': (0.0, 0.0),
      'levels_upper': (80.0, 85.0),
    },
    check_ruleset_name="acme_multiitem_percentage",
)


register.snmp_section(
    name = "acme_multiitem",
    detect = startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.9148"),
    parse_function=parse_acme_multiitem,
    fetch = SNMPTree(
      base = '.1.3.6.1.4.1.9148.3.2.1.1',
      oids = [
        "5",  # apSysGlobalConSess: The total instant number of Global Concurrent Sessions at the moment.
        "6",  # apSysGlobalCPS: The number of global call per second. This is an instant value.
        "11", # apSysSipStatsActiveLocalContacts: Number of current cached registered contacts in the SD.
      ],
    )
)

register.snmp_section(
    name = "acme_multiitem_percentage",
    detect = startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.9148"),
    parse_function=parse_acme_multiitem_percentage,
    fetch = SNMPTree(
      base = '.1.3.6.1.4.1.9148.3.2.1.1',
      oids = [
        "1",  # apSysCPUUtil: The percentage of total CPU utilization measured in 1 second.
        "2",  # apSysMemoryUtil: The percentage of Memory utilization
        "10", # apSysLicenseCapacity: The percentage of licensed sessions currently in progress.
      ],
    )
)
