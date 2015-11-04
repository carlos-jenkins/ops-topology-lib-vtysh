# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Hewlett Packard Enterprise Development LP
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

# WARNING: This is auto-generated, do not manually modify

"""
vtysh library.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

from .parser import *  # noqa


class ConfigInterfaceMgmt(object):
    """
    Configure management interface.
    """
    def __init__(self, enode):
        self.enode = enode

    def __enter__(self):
        commands = """\
            config terminal
            interface mgmt
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def ip_static(self, ip):
        """
        Set IP address

        This function runs the following vtysh command:
            # ip static {ip}

        :param ip: Interface IP (ipv4 or ipv6) address.
        """

        assert not self.enode(
            'ip static {ip}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ip_static(self, ip):
        """
        Unset IP address

        This function runs the following vtysh command:
            # no ip static {ip}

        :param ip: Interface IP (ipv4 or ipv6) address.
        """

        assert not self.enode(
            'no ip static {ip}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def default_gateway(self, gateway):
        """
        Configure the Default gateway address (IPv4 and IPv6)

        This function runs the following vtysh command:
            # default-gateway {gateway}

        :param gateway: IP (ipv4 or ipv6) address.
        """

        assert not self.enode(
            'default-gateway {gateway}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_default_gateway(self, gateway):
        """
        Remove the Default gateway address (IPv4 and IPv6)

        This function runs the following vtysh command:
            # no default-gateway {gateway}

        :param gateway: IP (ipv4 or ipv6) address.
        """

        assert not self.enode(
            'no default-gateway {gateway}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def nameserver(self, primary_nameserver, secondary_nameserver=''):
        """
        Configure the nameserver

        This function runs the following vtysh command:
            # nameserver {primary_nameserver} {secondary_nameserver}

        :param primary_nameserver: Primary nameserver (ipv4 or ipv6) address.
        :param secondary_nameserver: Secondary nameserver (ipv4 or ipv6)
            address.
        """

        assert not self.enode(
            'nameserver {primary_nameserver} {secondary_nameserver}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_nameserver(self, primary_nameserver, secondary_nameserver=''):
        """
        Configure the nameserver

        This function runs the following vtysh command:
            # no nameserver {primary_nameserver} {secondary_nameserver}

        :param primary_nameserver: Primary nameserver (ipv4 or ipv6) address.
        :param secondary_nameserver: Secondary nameserver (ipv4 or ipv6)
            address.
        """

        assert not self.enode(
            'no nameserver {primary_nameserver} {secondary_nameserver}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ip_dhcp(self):
        """
        Set the mode as dhcp.

        This function runs the following vtysh command:
            # ip dhcp

        """

        assert not self.enode(
            'ip dhcp'.format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigInterfaceVlan(object):
    """
    VLAN configuration.
    """
    def __init__(self, enode, vlan_id):
        self.enode = enode
        self.vlan_id = vlan_id

    def __enter__(self):
        commands = """\
            config terminal
            interface vlan {vlan_id}
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def ip_address(self, ipv4):
        """
        Set IP address

        This function runs the following vtysh command:
            # ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ip_address(self, ipv4):
        """
        Unset IP address

        This function runs the following vtysh command:
            # no ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'no ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ip_address_secondary(self, ipv4):
        """
        Set secondary IP address

        This function runs the following vtysh command:
            # ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ip_address_secondary(self, ipv4):
        """
        Unset secondary IP address

        This function runs the following vtysh command:
            # no ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'no ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ipv6_address(self, ipv6):
        """
        Set IPv6 address

        This function runs the following vtysh command:
            # ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ipv6_address(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:
            # no ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'no ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ipv6_address_secondary(self, ipv6):
        """
        Set secondary IPv6 address

        This function runs the following vtysh command:
            # ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ipv6_address_secondary(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:
            # no ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'no ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def shutdown(self):
        """
        Enable an interface.

        This function runs the following vtysh command:
            # shutdown

        """

        assert not self.enode(
            'shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_shutdown(self):
        """
        Disable an interface.

        This function runs the following vtysh command:
            # no shutdown

        """

        assert not self.enode(
            'no shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigInterface(object):
    """
    Interface configuration.
    """
    def __init__(self, enode, portlbl):
        self.enode = enode
        if portlbl not in enode.ports.keys():
            msg = 'Unknown portlbl, available portlbl are: {}'.format(
                  ', '.join('\'{}\''.format(k) for k in enode.ports.keys()))
            raise Exception(msg)
        self.port = enode.ports[portlbl]

    def __enter__(self):
        commands = """\
            config terminal
            interface {port}
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def ip_address(self, ipv4):
        """
        Set IP address

        This function runs the following vtysh command:
            # ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ip_address(self, ipv4):
        """
        Unset IP address

        This function runs the following vtysh command:
            # no ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'no ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ip_address_secondary(self, ipv4):
        """
        Set secondary IP address

        This function runs the following vtysh command:
            # ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ip_address_secondary(self, ipv4):
        """
        Unset secondary IP address

        This function runs the following vtysh command:
            # no ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'no ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ipv6_address(self, ipv6):
        """
        Set IPv6 address

        This function runs the following vtysh command:
            # ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ipv6_address(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:
            # no ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'no ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ipv6_address_secondary(self, ipv6):
        """
        Set secondary IPv6 address

        This function runs the following vtysh command:
            # ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ipv6_address_secondary(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:
            # no ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'no ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def routing(self):
        """
        Configure interface as L3.

        This function runs the following vtysh command:
            # routing

        """

        assert not self.enode(
            'routing'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_routing(self):
        """
        Unconfigure interface as L3.

        This function runs the following vtysh command:
            # no routing

        """

        assert not self.enode(
            'no routing'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def shutdown(self):
        """
        Enable an interface.

        This function runs the following vtysh command:
            # shutdown

        """

        assert not self.enode(
            'shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_shutdown(self):
        """
        Disable an interface.

        This function runs the following vtysh command:
            # no shutdown

        """

        assert not self.enode(
            'no shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def vlan_access(self, vlan_id):
        """
        Access configuration

        This function runs the following vtysh command:
            # vlan access {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        assert not self.enode(
            'vlan access {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_vlan_access(self, vlan_id):
        """
        Remove vlan access

        This function runs the following vtysh command:
            # no vlan access {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        assert not self.enode(
            'no vlan access {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def vlan_trunk_allowed(self, vlan_id):
        """
        Allow VLAN on the trunk port

        This function runs the following vtysh command:
            # vlan trunk allowed {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        assert not self.enode(
            'vlan trunk allowed {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_vlan_trunk_allowed(self, vlan_id):
        """
        Disallow VLAN on the trunk port

        This function runs the following vtysh command:
            # no vlan trunk allowed {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        assert not self.enode(
            'no vlan trunk allowed {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def vlan_trunk_native_tag(self):
        """
        Tag configuration on the trunk port

        This function runs the following vtysh command:
            # vlan trunk native tag

        """

        assert not self.enode(
            'vlan trunk native tag'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_vlan_trunk_native_tag(self):
        """
        Remove tag configuration on the trunk port

        This function runs the following vtysh command:
            # no vlan trunk native tag

        """

        assert not self.enode(
            'no vlan trunk native tag'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def vlan_trunk_native(self, vlan_id):
        """
        Native VLAN on the trunk port

        This function runs the following vtysh command:
            # vlan trunk native {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        assert not self.enode(
            'vlan trunk native {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_vlan_trunk_native(self, vlan_id):
        """
        Remove native VLAN on the trunk port

        This function runs the following vtysh command:
            # no vlan trunk native {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        assert not self.enode(
            'no vlan trunk native {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def lacp_port_id(self, port_id):
        """
        Set port ID used in LACP negotiation.

        This function runs the following vtysh command:
            # lacp port-id {port_id}

        :param port_id: <1-65535>  .The range is 1 to 65535
        """

        assert not self.enode(
            'lacp port-id {port_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def lacp_port_priority(self, port_priority):
        """
        Set port priority is used in LACP negotiation.

        This function runs the following vtysh command:
            # lacp port-priority {port_priority}

        :param port_priority: <1-65535>  The range is 1 to 65535
        """

        assert not self.enode(
            'lacp port-priority {port_priority}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def lag(self, lag_id):
        """
        Add the current interface to link aggregation.

        This function runs the following vtysh command:
            # lag {lag_id}

        :param lag_id: <1-2000>  LAG number ranges from 1 to 2000
        """

        assert not self.enode(
            'lag {lag_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_lag(self, lag_id):
        """
        Remove the current interface to link aggregation.

        This function runs the following vtysh command:
            # no lag {lag_id}

        :param lag_id: <1-2000>  LAG number ranges from 1 to 2000
        """

        assert not self.enode(
            'no lag {lag_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )


class Configure(object):
    """
    Configuration terminal
    """
    def __init__(self, enode):
        self.enode = enode

    def __enter__(self):
        commands = """\
            configure terminal
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def no_vlan(self, vlan_id):
        """
        Delete a VLAN

        This function runs the following vtysh command:
            # no vlan {vlan_id}

        :param vlan_id: VLAN Identifier.
        """

        assert not self.enode(
            'no vlan {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_interface_lag(self, lag_id):
        """
        Delete a lag

        This function runs the following vtysh command:
            # no interface lag {lag_id}

        :param lag_id: link-aggregation identifier.
        """

        assert not self.enode(
            'no interface lag {lag_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ip_route(self, ipv4, next_hop, metric=''):
        """
        Configure static routes

        This function runs the following vtysh command:
            # ip route {ipv4} {next_hop} {metric}

        :param ipv4: A.B.C.D/M IP destination prefix.
        :param next_hop: Can be an ip address or a interface.
        :param metric: Optional, route address to configure.
        """

        assert not self.enode(
            'ip route {ipv4} {next_hop} {metric}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ip_route(self, ipv4, next_hop, metric=''):
        """
        Un-configure static routes

        This function runs the following vtysh command:
            # no ip route {ipv4} {next_hop} {metric}

        :param ipv4: A.B.C.D/M IP destination prefix.
        :param next_hop: Can be an ip address or a interface.
        :param metric: Optional, route address to configure.
        """

        assert not self.enode(
            'no ip route {ipv4} {next_hop} {metric}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ipv6_route(self, ipv6, next_hop, metric=''):
        """
        Configure static routes

        This function runs the following vtysh command:
            # ipv6 route {ipv6} {next_hop} {metric}

        :param ipv6: X:X::X:X/M IP destination prefix.
        :param next_hop: Can be an ip address or a interface.
        :param metric: Optional, route address to configure.
        """

        assert not self.enode(
            'ipv6 route {ipv6} {next_hop} {metric}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ipv6_route(self, ipv6, next_hop, metric=''):
        """
        Un-configure static routes

        This function runs the following vtysh command:
            # no ipv6 route {ipv6} {next_hop} {metric}

        :param ipv6: X:X::X:X/M IP destination prefix.
        :param next_hop: Can be an ip address or a interface.
        :param metric: Optional, route address to configure.
        """

        assert not self.enode(
            'no ipv6 route {ipv6} {next_hop} {metric}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def lacp_system_priority(self, priority):
        """
        Set LACP system priority.

        This function runs the following vtysh command:
            # lacp system-priority {priority}

        :param priority: <0-65535>  The range is 0 to 65535.
        """

        assert not self.enode(
            'lacp system-priority {priority}'.format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigInterfaceLag(object):
    """
    Configure link-aggregation parameters.
    """
    def __init__(self, enode, lag):
        self.enode = enode
        self.lag = lag

    def __enter__(self):
        commands = """\
            config terminal
            interface lag {lag}
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def ip_address(self, ipv4):
        """
        Set IP address

        This function runs the following vtysh command:
            # ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ip_address(self, ipv4):
        """
        Unset IP address

        This function runs the following vtysh command:
            # no ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'no ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ip_address_secondary(self, ipv4):
        """
        Set secondary IP address

        This function runs the following vtysh command:
            # ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ip_address_secondary(self, ipv4):
        """
        Unset secondary IP address

        This function runs the following vtysh command:
            # no ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        assert not self.enode(
            'no ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ipv6_address(self, ipv6):
        """
        Set IPv6 address

        This function runs the following vtysh command:
            # ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ipv6_address(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:
            # no ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'no ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def ipv6_address_secondary(self, ipv6):
        """
        Set secondary IPv6 address

        This function runs the following vtysh command:
            # ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_ipv6_address_secondary(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:
            # no ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        assert not self.enode(
            'no ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def shutdown(self):
        """
        Enable an interface.

        This function runs the following vtysh command:
            # shutdown

        """

        assert not self.enode(
            'shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_shutdown(self):
        """
        Disable an interface.

        This function runs the following vtysh command:
            # no shutdown

        """

        assert not self.enode(
            'no shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def lacp_mode_passive(self):
        """
        Sets an interface as LACP passive.

        This function runs the following vtysh command:
            # lacp mode passive

        """

        assert not self.enode(
            'lacp mode passive'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_lacp_mode_passive(self):
        """
        Sets an LACP passive interface off.

        This function runs the following vtysh command:
            # no lacp mode passive

        """

        assert not self.enode(
            'no lacp mode passive'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def lacp_mode_active(self):
        """
        Sets an interface as LACP active.

        This function runs the following vtysh command:
            # lacp mode active

        """

        assert not self.enode(
            'lacp mode active'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_lacp_mode_active(self):
        """
        Sets an LACP active interface off.

        This function runs the following vtysh command:
            # no lacp mode active

        """

        assert not self.enode(
            'no lacp mode active'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def lacp_fallback(self):
        """
        Enable LACP fallback mode.

        This function runs the following vtysh command:
            # lacp fallback

        """

        assert not self.enode(
            'lacp fallback'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def hash_l2_src_dst(self):
        """
        Base the hash on l2-src-dst.

        This function runs the following vtysh command:
            # hash l2-src-dst

        """

        assert not self.enode(
            'hash l2-src-dst'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def hash_l3_src_dst(self):
        """
        Base the hash on l3-src-dst.

        This function runs the following vtysh command:
            # hash l3-src-dst

        """

        assert not self.enode(
            'hash l3-src-dst'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def lacp_rate_fast(self):
        """
        Set LACP heartbeats are requested at the rate of one per second.

        This function runs the following vtysh command:
            # lacp rate fast

        """

        assert not self.enode(
            'lacp rate fast'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_lacp_rate_fast(self):
        """
        Set LACP heartbeats slow which is once every  30 seconds.

        This function runs the following vtysh command:
            # no lacp rate fast

        """

        assert not self.enode(
            'no lacp rate fast'.format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigVlan(object):
    """
    VLAN configuration.
    """
    def __init__(self, enode, vlan_id):
        self.enode = enode
        self.vlan_id = vlan_id

    def __enter__(self):
        commands = """\
            config terminal
            vlan {vlan_id}
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def shutdown(self):
        """
        Enable the VLAN.

        This function runs the following vtysh command:
            # shutdown

        """

        assert not self.enode(
            'shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_shutdown(self):
        """
        Disable the VLAN.

        This function runs the following vtysh command:
            # no shutdown

        """

        assert not self.enode(
            'no shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )


def show_interface(enode, portlbl):
    """
    Interface infomation.

    This function runs the following vtysh command:
        # show interface {port}

    :param portlbl: Label that identifies interface.
    :return: parse_show_interface(raw_result)
    """
    if portlbl not in enode.ports.keys():
        msg = 'Unknown portlbl, available portlbl are: {}'.format(
              ', '.join('\'{}\''.format(k) for k in enode.ports.keys()))
        raise Exception(msg)
    port = enode.ports[portlbl]

    return parse_show_interface(enode(
        'show interface {port}'.format(**locals()),
        shell='vtysh'
    ))


def show_vlan(enode):
    """
    Show VLAN configuration.

    This function runs the following vtysh command:
        # show vlan

    :return: parse_show_vlan(raw_result)
    """

    return parse_show_vlan(enode(
        'show vlan'.format(**locals()),
        shell='vtysh'
    ))


def show_lacp_interface(enode, portlbl):
    """
    Show LACP interface.

    This function runs the following vtysh command:
        # show lacp interface {port}

    :param portlbl: Label that identifies interface.
    :return: parse_show_lacp_interface(raw_result)
    """
    if portlbl not in enode.ports.keys():
        msg = 'Unknown portlbl, available portlbl are: {}'.format(
              ', '.join('\'{}\''.format(k) for k in enode.ports.keys()))
        raise Exception(msg)
    port = enode.ports[portlbl]

    return parse_show_lacp_interface(enode(
        'show lacp interface {port}'.format(**locals()),
        shell='vtysh'
    ))


def show_lacp_aggregates(enode, lag=''):
    """
    Show LACP aggregates.

    This function runs the following vtysh command:
        # show lacp aggregates {lag}

    :param lag: Link-aggregate name.
    :return: parse_show_lacp_aggregates(raw_result)
    """

    return parse_show_lacp_aggregates(enode(
        'show lacp aggregates {lag}'.format(**locals()),
        shell='vtysh'
    ))


__all__ = [
    'ConfigInterfaceMgmt',
    'ConfigInterfaceVlan',
    'ConfigInterface',
    'Configure',
    'ConfigInterfaceLag',
    'ConfigVlan',
    'show_interface',
    'show_vlan',
    'show_lacp_interface',
    'show_lacp_aggregates'
]
