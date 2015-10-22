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


def interface(
        enode, portlbl,
        ipv4=None, ipv6=None, vlan=None, routing=None, shutdown=None):
    """
    Configure a interface.

    This communication library function allows to configure a interface.

    #. Setup a IPv4 address.
    #. Setup a IPv6 address.
    #. Setup a VLAN for the interface.
    #. Enable or disable routing.
    #. Bring up or down the interface.

    All parameters left as ``None`` are ignored and thus no configuration
    action is taken for that parameter (left "as-is").

    :param enode: Engine node to communicate with.
    :type enode: topology.platforms.base.BaseNode
    :param str portlbl: Port label to configure. Port label will be mapped to
     real port automatically.
    :param str ipv4: IPv4 address and netmask to assign to the interface in
     the form ``'192.168.20.20/24'``.
    :param str ipv6: IPv6 address and subnets to assign to the interface in
     the form ``'2001::1/120'``.
    :param int vlan: Vlan number to give this interface access to.
    :param bool routing: Enable or disable routing in this interface.
    :param bool shutdown: Bring up or down the interface.
    """

    # autonegotiation  Configure auto-negotiation process for the interface
    # duplex           Configure the interface duplex mode
    # flowcontrol      Configure interface flow control
    # ip               IP information
    # ipv6             IPv6 information
    # lacp             Configure LACP parameters
    # lag              Add the current interface to link aggregation
    # lldp             Configure LLDP parameters
    # mtu              Configure mtu for the interface
    # routing          Configure interface as L3
    # shutdown         Enable/disable an interface
    # speed            Configure the interface speed
    # split            Configure QSFP interface for 4x 10Gb operation or
    #                  1x 40Gb operation.
    # vlan             VLAN configuration
    # vrf              VRF Configuration

    assert portlbl
    port = enode.ports[portlbl]

    preamble = """\
        configure terminal
        interface {port}
    """

    try:
        enode.libs.assert_batch(preamble, locals(), shell='vtysh')

        if ipv4 is not None:
            ipv4_cmd = 'ip address {}'.format(ipv4)
            assert not enode(ipv4_cmd, shell='vtysh')

        if ipv6 is not None:
            ipv6_cmd = 'ipv6 address {}'.format(ipv6)
            assert not enode(ipv6_cmd, shell='vtysh')

        if vlan is not None:
            vlan_cmd = 'vlan access {}'.format(vlan)
            assert not enode(vlan_cmd, shell='vtysh')

        if routing is not None:
            routing_cmd = '{}routing'.format('' if routing else 'no ')
            assert not enode(routing_cmd, shell='vtysh')

        if shutdown is not None:
            shutdown_cmd = '{}shutdown'.format('' if shutdown else 'no ')
            assert not enode(shutdown_cmd, shell='vtysh')

    finally:
        assert not enode('end', shell='vtysh')


def vlan(enode, vlan, shutdown=None, description=None):
    """
    Configure a vlan.

    All parameters left as ``None`` are ignored and thus no configuration
    action is taken for that parameter (left "as-is").

    :param enode: Engine node to communicate with.
    :type enode: topology.platforms.base.BaseNode
    :param int vlan: Vlan number to setup.
    :param bool shutdown: Bring up or down the interface.
    :param str description: One (1) word describing the VLAN.
    """

    preamble = """\
        configure terminal
        vlan {vlan}
    """

    try:
        enode.libs.assert_batch(preamble, locals(), shell='vtysh')

        if shutdown is not None:
            shutdown_cmd = '{}shutdown'.format('' if shutdown else 'no ')
            assert not enode(shutdown_cmd, shell='vtysh')

        if description is not None:
            description_cmd = 'description {}'.format(description)
            assert not enode(description_cmd, shell='vtysh')

    finally:
        assert not enode('end', shell='vtysh')


def ipv4_route(enode, destination, nexthop):
    """
    Configure a IPv4 static route.

    All parameters left as ``None`` are ignored and thus no configuration
    action is taken for that parameter (left "as-is").

    :param enode: Engine node to communicate with.
    :type enode: topology.platforms.base.BaseNode
    :param str destination: IPv4 destination prefix in the form
     ``'10.0.0.0/8'``.
    :param str nexthop: Nexthop IPv4 (in the form ``'10.0.0.1'``) or outgoing
     interface.
    """

    preamble = """\
        configure terminal
        ip route {destination} {nexthop}
    """

    try:
        enode.libs.assert_batch(preamble, locals(), shell='vtysh')
    finally:
        assert not enode('end', shell='vtysh')


def del_ipv4_route(enode, destination, nexthop):
    """
    Remove a IPv4 static route.

    All parameters left as ``None`` are ignored and thus no configuration
    action is taken for that parameter (left "as-is").

    :param enode: Engine node to communicate with.
    :type enode: topology.platforms.base.BaseNode
    :param str destination: IPv4 destination prefix in the form
     ``'10.0.0.0/8'``.
    :param str nexthop: Nexthop IPv4 (in the form ``'10.0.0.1'``) or outgoing
     interface.
    """

    preamble = """\
        configure terminal
        no ip route {destination} {nexthop}
    """

    try:
        enode.libs.assert_batch(preamble, locals(), shell='vtysh')
    finally:
        assert not enode('end', shell='vtysh')


def ipv6_route(enode, destination, nexthop):
    """
    Configure a IPv6 static route.

    All parameters left as ``None`` are ignored and thus no configuration
    action is taken for that parameter (left "as-is").

    :param enode: Engine node to communicate with.
    :type enode: topology.platforms.base.BaseNode
    :param str destination: IPv6 destination prefix in the form
     ``'2010:bd9::/32'``.
    :param str nexthop: Nexthop IPv6 (in the form ``'2010:bda::'``) or outgoing
     interface.
    """

    preamble = """\
        configure terminal
        ipv6 route {destination} {nexthop}
    """

    try:
        enode.libs.assert_batch(preamble, locals(), shell='vtysh')
    finally:
        assert not enode('end', shell='vtysh')


__all__ = [
    'interface',
    'vlan',
    'ipv4_route',
    'ipv6_route'
]
