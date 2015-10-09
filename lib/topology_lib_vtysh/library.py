# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Hewlett Packard Enterprise Development LP <asicapi@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
topology_lib_vtysh communication library implementation.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division


def configure_interface(enode, ipv4=None, portlbl=None, up=None):
    """
    Configure a interface.

    This communication library function allows to:

    #. Set address if given interface.
    #. Bring up or down the interface, or leave it as it is.

    :param enode: Engine node to communicate with.
    :type enode: topology.platforms.base.BaseNode
    :param str ipv4: IPv4 address and netmask to assign to the interface in
     the form ``'192.168.20.20/24'``.
    :param str portlbl: Port label to configure. Port label will be mapped to
     real port automatically.
    :param up: Bring up or down the interface. If ``None``, take no action.
    :type up: bool or None
    """
    assert ipv4 is not None
    assert portlbl is not None

    commands = """\
        configure terminal
        interface {port}
        ip address {ipv4}
    """
    replace = {
        'port': enode.ports[portlbl],
        'ipv4': ipv4
    }

    try:
        enode.libs.assert_batch(commands, replace=replace, shell='vtysh')
        if up is not None:
            shutdown = '{}shutdown'.format('no ' if up else '')
            enode(shutdown, shell='vtysh')

    finally:
        assert not enode('end', shell='vtysh')


__all__ = [
    'configure_interface'
]
