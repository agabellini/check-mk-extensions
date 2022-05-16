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
# <<<slapd_stats_statistics:sep(44)>>>
# ldap-slave1,Entries,111386
# ldap-slave1,Referrals,0
# ldap-slave1,PDU,213505
# ldap-slave1,Bytes,17979195

from .agent_based_api.v1 import *
import time

map_metric = {
  'Entries':   'slapd_entries_sent',
  'Referrals': 'slapd_referrals_sent',
  'PDU':       'slapd_pdu_sent',
  'Bytes':     'net_data_sent'
}


def parse_slapd_stats_statistics(string_table):
    return string_table


def discover_slapd_stats_statistics(section):
    for name, _op, _value in section:
      yield Service(item=name)


def check_slapd_stats_statistics(item, params, section):
    for name, _op, _value in section:
      if item == name:
        _value = int(_value)
        warn, crit = params[_op]

        this_time = int(time.time())
        value_store = get_value_store()
        rate = get_rate(value_store, "slapd.stats.statistics.%s" % _op, this_time, _value)

        yield from check_levels(
          float(rate),
          levels_upper=(warn, crit),
          metric_name=map_metric[_op],
          render_func=lambda v: "%.2f/s" % v,
          label="Rate of sent %s" % _op,
          boundaries=(0, None),
        )

    return


register.check_plugin(
    name="slapd_stats_statistics",
    service_name="SLAPD %s Statistics",
    discovery_function=discover_slapd_stats_statistics,
    check_function=check_slapd_stats_statistics,
    check_default_parameters = {
      "Entries": (None, None),
      "Referrals": (None, None),
      "PDU": (None, None),
      "Bytes": (None, None),
    },
    check_ruleset_name="slapd_stats_statistics"
)


register.agent_section(
    name = "slapd_stats_statistics",
    parse_function = parse_slapd_stats_statistics,
)
