# Copyright 2018 Red Hat, Inc
# Copyright 2017 Rackspace Australia
# Copyright 2018 Michael Still and Aptira
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Helpers for filesystem related routines.
"""


from oslo_concurrency import processutils

import cinder.privsep


@cinder.privsep.sys_admin_pctxt.entrypoint
def umount(mountpoint):
    processutils.execute('umount', mountpoint, attempts=1, delay_on_retry=True)


@cinder.privsep.sys_admin_pctxt.entrypoint
def truncate(size, path):
    processutils.execute('truncate', '-s', size, path)
