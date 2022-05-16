#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: GNU General Public License v2

from cmk.gui.plugins.metrics import check_metrics
from cmk.gui.plugins.metrics.translation import df_translation

check_metrics["check_mk-acme_fs"] = df_translation
OMD[nagtism]:~/local/lib/check_mk/base/plugins/agent_based$ cat acme_fs.py
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

from .utils.df import (
    df_check_filesystem_single,
    FILESYSTEM_DEFAULT_LEVELS,
)


def discover_acme_fs(section):
    for name, _total, _avail in section:
      yield Service(item=name)


def check_acme_fs(item, params, section):
    for name, total, avail in section:
      if name == item:
        total = int(total)
        avail = int(int(avail) / 1024)

        yield from df_check_filesystem_single(
          value_store=get_value_store(),
          mountpoint=item,
          size_mb=total,
          avail_mb=avail,
          reserved_mb=0,
          inodes_total=None,
          inodes_avail=None,
          params=params,
        )

        return


register.check_plugin(
    name="acme_fs",
    service_name="Filesystem %s",
    discovery_function=discover_acme_fs,
    check_function=check_acme_fs,
    check_default_parameters = FILESYSTEM_DEFAULT_LEVELS,
    check_ruleset_name="filesystem",
)


register.snmp_section(
    name = "acme_fs",
    detect = startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.9148"),
    fetch = SNMPTree(
      base = '.1.3.6.1.4.1.9148.3.2.1.1.23.1',
      oids = [
        #"1",  # apSysVolumeIndex
        "2",  # apSysVolumeName
        "3",  # apSysVolumeTotalSpace, The total size of the volume, in MB
        "4",  # apSysVolumeAvailSpace, The total space available on the volume, in KB
      ],
    )
)
