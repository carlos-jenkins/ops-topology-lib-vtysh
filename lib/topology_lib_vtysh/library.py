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


class ContextManager(object):
    """
    This class defines a context manager object.

    Usage:

    ::

        with ClassName(parameters) as ctx:
            ctx.first_function()
            ctx.second_function()

    This way at the beginning the **pre_commands** will be run and at the end
    the **post_commands** will clean the vtysh terminal. Every implementation
    of this class document their pre_commands and post_commands.

    """


class Configure(ContextManager):
    """
    Configuration terminal

    pre_commands:

    ::

            ['configure terminal']

    post_commands:

    ::

            ['end']
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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

            # lacp system-priority {priority}

        :param priority: <0-65535>  The range is 0 to 65535.
        """

        assert not self.enode(
            'lacp system-priority {priority}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def feature_lldp(self):
        """
        Configure LLDP parameters.

        This function runs the following vtysh command:

        ::

            # feature lldp

        """

        assert not self.enode(
            'feature lldp'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_feature_lldp(self):
        """
        Un-configure LLDP parameters.

        This function runs the following vtysh command:

        ::

            # no feature lldp

        """

        assert not self.enode(
            'no feature lldp'.format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigInterface(ContextManager):
    """
    Interface configuration.

    pre_commands:

    ::

            ['config terminal', 'interface {port}']

    post_commands:

    ::

            ['end']
    """

    def __init__(self, enode, portlbl):
        self.enode = enode
        self.port = enode.ports.get(portlbl, portlbl)

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

            # no lag {lag_id}

        :param lag_id: <1-2000>  LAG number ranges from 1 to 2000
        """

        assert not self.enode(
            'no lag {lag_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def lldp_transmission(self):
        """
        Set the transmission on lldp.

        This function runs the following vtysh command:

        ::

            # lldp transmission

        """

        assert not self.enode(
            'lldp transmission'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_lldp_transmission(self):
        """
        Un-set the transmission on lldp.

        This function runs the following vtysh command:

        ::

            # no lldp transmission

        """

        assert not self.enode(
            'no lldp transmission'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def lldp_reception(self):
        """
        Set the reception on lldp.

        This function runs the following vtysh command:

        ::

            # lldp reception

        """

        assert not self.enode(
            'lldp reception'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_lldp_reception(self):
        """
        Un-set the reception on lldp.

        This function runs the following vtysh command:

        ::

            # no lldp reception

        """

        assert not self.enode(
            'no lldp reception'.format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigInterfaceVlan(ContextManager):
    """
    VLAN configuration.

    pre_commands:

    ::

            ['config terminal', 'interface vlan {vlan_id}']

    post_commands:

    ::

            ['end']
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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

            # no shutdown

        """

        assert not self.enode(
            'no shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigInterfaceLag(ContextManager):
    """
    Configure link-aggregation parameters.

    pre_commands:

    ::

            ['config terminal', 'interface lag {lag}']

    post_commands:

    ::

            ['end']
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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

            # no shutdown

        """

        assert not self.enode(
            'no shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def routing(self):
        """
        Configure interface as L3.

        This function runs the following vtysh command:

        ::

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

        ::

            # no routing

        """

        assert not self.enode(
            'no routing'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def vlan_access(self, vlan_id):
        """
        Access configuration

        This function runs the following vtysh command:

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

            # no vlan trunk native {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        assert not self.enode(
            'no vlan trunk native {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def lacp_mode_passive(self):
        """
        Sets an interface as LACP passive.

        This function runs the following vtysh command:

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

            # no lacp rate fast

        """

        assert not self.enode(
            'no lacp rate fast'.format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigInterfaceMgmt(ContextManager):
    """
    Configure management interface.

    pre_commands:

    ::

            ['config terminal', 'interface mgmt']

    post_commands:

    ::

            ['end']
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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

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

        ::

            # ip dhcp

        """

        assert not self.enode(
            'ip dhcp'.format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigRouterBgp(ContextManager):
    """
    BGP configuration.

    pre_commands:

    ::

            ['config terminal', 'router bgp {asn}']

    post_commands:

    ::

            ['end']
    """

    def __init__(self, enode, asn):
        self.enode = enode
        self.asn = asn

    def __enter__(self):
        commands = """\
            config terminal
            router bgp {asn}
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

    def bgp_router_id(self, id):
        """
        Specifies the BGP router-ID for a BGP Router

        This function runs the following vtysh command:

        ::

            # bgp router-id {id}

        :param id: <A.B.C.D> IPv4 address
        """

        assert not self.enode(
            'bgp router-id {id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_bgp_router_id(self, id):
        """
        Removes the BGP router-ID for a BGP Router

        This function runs the following vtysh command:

        ::

            # no bgp router-id {id}

        :param id: <A.B.C.D> IPv4 address
        """

        assert not self.enode(
            'no bgp router-id {id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def network(self, network):
        """
        Adds the announcement network for BGP

        This function runs the following vtysh command:

        ::

            # network {network}

        :param network: <A.B.C.D/M> IPv4 address with the prefix len
        """

        assert not self.enode(
            'network {network}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_network(self, network):
        """
        Removes the announcement network for BGP

        This function runs the following vtysh command:

        ::

            # no network {network}

        :param network: <A.B.C.D/M> IPv4 address with the prefix length
        """

        assert not self.enode(
            'no network {network}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def maximum_paths(self, num):
        """
        Sets the maximum number of paths for a BGP route

        This function runs the following vtysh command:

        ::

            # maximum-paths {num}

        :param num: <1-255> Maximum number of paths. Default is 1
        """

        assert not self.enode(
            'maximum-paths {num}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_maximum_paths(self, num):
        """
        Set the max number of paths to the default value of 1

        This function runs the following vtysh command:

        ::

            # no maximum-paths {num}

        :param num: <1-255> Maximum number of paths. Default is 1
        """

        assert not self.enode(
            'no maximum-paths {num}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def timers_bgp(self, keepalive, hold):
        """
        Sets the keepalive interval and hold time for a BGP router

        This function runs the following vtysh command:

        ::

            # timers bgp {keepalive} {hold}

        :param keepalive: <0-65535> Keepalive interval in seconds. Default is
            60
        :param hold: <0 - 65535> Hold time in seconds. Default is 180
        """

        assert not self.enode(
            'timers bgp {keepalive} {hold}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_timers_bgp(self, keepalive='', hold=''):
        """
        Sets the default values for keepalive interval and hold time for a BGP
        router

        This function runs the following vtysh command:

        ::

            # no timers bgp {keepalive} {hold}

        :param keepalive: <0 - 65535> Keepalive interval in seconds. Default
            is 60
        :param hold: <0 - 65535> Hold time in seconds. Default is 180
        """

        assert not self.enode(
            'no timers bgp {keepalive} {hold}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def neighbor_remote_as(self, ip, asn):
        """
        Configures a BGP neighbor

        This function runs the following vtysh command:

        ::

            # neighbor {ip} remote-as {asn}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param asn: <1 - 4294967295> Neighbor AS number. Ranges from 1 to
            4294967295
        """

        assert not self.enode(
            'neighbor {ip} remote-as {asn}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_neighbor_remote_as(self, ip, asn):
        """
        Removes a BGP neighbor

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} remote-as {asn}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param asn: <1 - 4294967295> Neighbor AS number. Ranges from 1 to
            4294967295
        """

        assert not self.enode(
            'no neighbor {ip} remote-as {asn}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def neighbor_description(self, ip, text):
        """
        Removes a BGP neighbor

        This function runs the following vtysh command:

        ::

            # neighbor {ip} description {text}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param text: Description of the peer router. String of maximum length
            80 chars
        """

        assert not self.enode(
            'neighbor {ip} description {text}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_neighbor_description(self, ip, text=''):
        """
        Removes a BGP neighbor

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} description {text}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param text: Description of the peer router.String of maximum length
            80 chars
        """

        assert not self.enode(
            'no neighbor {ip} description {text}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def neighbor_password(self, ip, pwd):
        """
        Enables MD5 authentication on a TCP connection between BGP peers.

        This function runs the following vtysh command:

        ::

            # neighbor {ip} password {pwd}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param pwd: Password in plain text.String of maximum length 80 chars
        """

        assert not self.enode(
            'neighbor {ip} password {pwd}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_neighbor_password(self, ip, pwd=''):
        """
        Removes MD5 authentication on a TCP connection between BGP peers.

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} password {pwd}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param pwd: Password in plain text.String of maximum length 80 chars
        """

        assert not self.enode(
            'no neighbor {ip} password {pwd}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def neighbor_timers(self, ip, keepalive, hold):
        """
        Sets the keepalive interval and hold time for a specific BGP peer

        This function runs the following vtysh command:

        ::

            # neighbor {ip} timers {keepalive} {hold}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param keepalive: <0 - 65535> Keepalive interval in seconds.Default is
            60
        :param hold: <0-65535> Hold time in seconds. Default is 180
        """

        assert not self.enode(
            'neighbor {ip} timers {keepalive} {hold}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_neighbor_timers(self, ip, keepalive='', hold=''):
        """
        Sets the default values for keepalive interval and hold time for a
        specific BGP peer

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} timers {keepalive} {hold}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param keepalive: <0 - 65535> Keepalive interval in seconds.Default is
            0
        :param hold: <0 - 65535> Hold time in seconds. Default is 0
        """

        assert not self.enode(
            'no neighbor {ip} timers {keepalive} {hold}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def neighbor_allowas_in(self, ip, val=''):
        """
        Specifies an allow-as-in occurrence number for an AS to be in the AS
        path

        This function runs the following vtysh command:

        ::

            # neighbor {ip} allowas-in {val}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param val: <0 - 10> Number of times BGP can allow an instance of AS
            to be in the AS_PATH
        """

        assert not self.enode(
            'neighbor {ip} allowas-in {val}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_neighbor_allowas_in(self, ip, val=''):
        """
        Clears the allow-as-in occurrence number for an AS to be in the AS path

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} allowas-in {val}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param val: <0 - 10> Number of times BGP can allow aninstance of AS to
            be in the AS_PATH
        """

        assert not self.enode(
            'no neighbor {ip} allowas-in {val}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def neighbor_remove_private_as(self, ip):
        """
        Removes private AS numbers from the AS pathin outbound routing updates

        This function runs the following vtysh command:

        ::

            # neighbor {ip} remove-private-AS

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        assert not self.enode(
            'neighbor {ip} remove-private-AS'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_neighbor_remove_private_as(self, ip):
        """
        Resets to a cleared state (default)

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} remove-private-AS

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        assert not self.enode(
            'no neighbor {ip} remove-private-AS'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def neighbor_soft_reconfiguration_inbound(self, ip):
        """
        Enables software-based reconfiguration to generate updates from a
        neighbor without clearing the BGP session

        This function runs the following vtysh command:

        ::

            # neighbor {ip} soft-reconfiguration inbound

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        assert not self.enode(
            'neighbor {ip} soft-reconfiguration inbound'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_neighbor_soft_reconfiguration_inbound(self, ip):
        """
        Resets to a cleared state (default)

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} soft-reconfiguration inbound

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        assert not self.enode(
            'no neighbor {ip} soft-reconfiguration inbound'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def neighbor_shutdown(self, ip):
        """
        Shuts down the neighbor. This disables the peer routerbut preserves
        neighbor configuration

        This function runs the following vtysh command:

        ::

            # neighbor {ip} shutdown

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        assert not self.enode(
            'neighbor {ip} shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_neighbor_shutdown(self, ip):
        """
        Re-enables the neighbor

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} shutdown

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        assert not self.enode(
            'no neighbor {ip} shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def neighbor_peer_group(self, ip_or_group, group=''):
        """
        Assigns a neighbor to a peer-group

        This function runs the following vtysh command:

        ::

            # neighbor {ip_or_group} peer-group {group}

        :param ip_or_group: <A.B.C.D> Neighbor IPv4 address<X:X::X:X> Neighbor
            IPv6 address<WORD> Neighbor group
        :param group: ('Peer-group name.String of maximum length 80 chars',)
        """

        assert not self.enode(
            'neighbor {ip_or_group} peer-group {group}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_neighbor_peer_group(self, ip_or_group, group=''):
        """
        Removes the neighbor from the peer-group

        This function runs the following vtysh command:

        ::

            # no neighbor {ip_or_group} peer-group {group}

        :param ip_or_group: <A.B.C.D> Neighbor IPv4 address<X:X::X:X> Neighbor
            IPv6 address<WORD> Neighbor group
        :param group: Peer-group name. String of maximum length 80 chars
        """

        assert not self.enode(
            'no neighbor {ip_or_group} peer-group {group}'.format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigVlan(ContextManager):
    """
    VLAN configuration.

    pre_commands:

    ::

            ['config terminal', 'vlan {vlan_id}']

    post_commands:

    ::

            ['end']
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

        ::

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

        ::

            # no shutdown

        """

        assert not self.enode(
            'no shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def description(self, description):
        """
        Set VLAN description

        This function runs the following vtysh command:

        ::

            # description {description}

        :param description: VLAN description.
        """

        assert not self.enode(
            'description {description}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_description(self, description):
        """
        Un-set VLAN description

        This function runs the following vtysh command:

        ::

            # no description {description}

        :param description: VLAN description.
        """

        assert not self.enode(
            'no description {description}'.format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigDhcp(ContextManager):
    """
    DHCP configuration.

    pre_commands:

    ::

            ['config terminal', 'dhcp-server']

    post_commands:

    ::

            ['end']
    """

    def __init__(self, enode):
        self.enode = enode

    def __enter__(self):
        commands = """\
            config terminal
            dhcp-server
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

    def option_number(self, opt_number, opt_value):
        """
        Set DHCP option number with value

        This function runs the following vtysh command:

        ::

            # option set option-number {opt_number} option-value {opt_value}

        :param opt_number: 0-255 Option number for DHCP server
        :param opt_value: Text for the value of DHCP option
        """

        assert not self.enode(
            ' '.join(['option set option-number {opt_number} option-value',
                      '{opt_value}']).format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_option_number(self, opt_number, opt_value):
        """
        Unset DHCP option number with value

        This function runs the following vtysh command:

        ::

            # no option set option-number {opt_number} option-value
                {opt_value}

        :param opt_number: 0-255 Option number for DHCP server
        :param opt_value: Text for the value of DHCP option
        """

        assert not self.enode(
            ' '.join('no option set option-number {opt_number} option-value',
                     '{opt_value}').format(
                **locals()
            ),
            shell='vtysh'
        )

    def range(self, name, start, end, netmask):
        """
        Set DHCP range

        This function runs the following vtysh command:

        ::

            # range {name} start-ip-address {start} end-ip-address {end}
                netmask {netmask}

        :param opt_number: 0-255 Option number for DHCP server
        :param opt_value: Text for the value of DHCP option
        """

        assert not self.enode(
            ' '.join(['range {name} start-ip-address {start} end-ip-address',
                      '{end} netmask {netmask}']).format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_range(self, name, start, end, netmask):
        """
        Set DHCP range

        This function runs the following vtysh command:

        ::

            # range {name} start-ip-address {start} end-ip-address {end}
                netmask {netmask}

        :param opt_number: 0-255 Option number for DHCP server
        :param opt_value: Text for the value of DHCP option
        """

        assert not self.enode(
            ' '.join(['no range {name} start-ip-address {start}',
                      'end-ip-address {end} netmask {netmask}']).format(
                **locals()
            ),
            shell='vtysh'
        )


class ConfigTftp(ContextManager):
    """
    TFTP configuration.

    pre_commands:

    ::

            ['config terminal', 'tftp-server']

    post_commands:

    ::

            ['end']
    """

    def __init__(self, enode):
        self.enode = enode

    def __enter__(self):
        commands = """\
            config terminal
            tftp-server
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

    def path(self, path):
        """
        Set TFTP server folder path

        This function runs the following vtysh command:

        ::

            # path {path}

        :param path: /path/to/files Folder where files are served
        """

        assert not self.enode(
            'path {path}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_path(self, path):
        """
        Unset TFTP server folder path

        This function runs the following vtysh command:

        ::

            # no path {path}

        :param path: /path/to/files Folder where files are served
        """

        assert not self.enode(
            'no path {path}'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def enable(self):
        """
        Enable TFTP server

        This function runs the following vtysh command:

        ::

            # enable

        """

        assert not self.enode(
            'enable'.format(
                **locals()
            ),
            shell='vtysh'
        )

    def no_enable(self):
        """
        Disable TFTP server

        This function runs the following vtysh command:

        ::

            # no enable

        """

        assert not self.enode(
            'no enable'.format(
                **locals()
            ),
            shell='vtysh'
        )


def show_interface(enode, portlbl):
    """
    Interface infomation.

    This function runs the following vtysh command:

    ::

        # show interface {port}

    :param portlbl: Label that identifies interface.
    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_interface`
    """
    port = enode.ports.get(portlbl, portlbl)

    return parse_show_interface(enode(
        'show interface {port}'.format(**locals()),
        shell='vtysh'
    ))


def show_vlan(enode):
    """
    Show VLAN configuration.

    This function runs the following vtysh command:

    ::

        # show vlan

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_vlan`
    """

    return parse_show_vlan(enode(
        'show vlan'.format(**locals()),
        shell='vtysh'
    ))


def show_lacp_interface(enode, portlbl):
    """
    Show LACP interface.

    This function runs the following vtysh command:

    ::

        # show lacp interface {port}

    :param portlbl: Label that identifies interface.
    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_lacp_interface`
    """
    port = enode.ports.get(portlbl, portlbl)

    return parse_show_lacp_interface(enode(
        'show lacp interface {port}'.format(**locals()),
        shell='vtysh'
    ))


def show_lacp_aggregates(enode, lag=''):
    """
    Show LACP aggregates.

    This function runs the following vtysh command:

    ::

        # show lacp aggregates {lag}

    :param lag: Link-aggregate name.
    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_lacp_aggregates`
    """

    return parse_show_lacp_aggregates(enode(
        'show lacp aggregates {lag}'.format(**locals()),
        shell='vtysh'
    ))


def show_lacp_configuration(enode):
    """
    Show LACP configuration.

    This function runs the following vtysh command:

    ::

        # show lacp configuration

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_lacp_configuration`
    """

    return parse_show_lacp_configuration(enode(
        'show lacp configuration'.format(**locals()),
        shell='vtysh'
    ))


def show_lldp_neighbor_info(enode, portlbl):
    """
    Show global LLDP neighbor information.

    This function runs the following vtysh command:

    ::

        # show lldp neighbor-info {port}

    :param portlbl: Label that identifies interface.
    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_lldp_neighbor_info`
    """
    port = enode.ports.get(portlbl, portlbl)

    return parse_show_lldp_neighbor_info(enode(
        'show lldp neighbor-info {port}'.format(**locals()),
        shell='vtysh'
    ))


def show_lldp_statistics(enode):
    """
    Show LLDP statistics.

    This function runs the following vtysh command:

    ::

        # show lldp statistics

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_lldp_statistics`
    """

    return parse_show_lldp_statistics(enode(
        'show lldp statistics'.format(**locals()),
        shell='vtysh'
    ))


def show_ip_bgp_summary(enode):
    """
    Show bgp neighbors information summary.

    This function runs the following vtysh command:

    ::

        # show ip bgp summary

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_ip_bgp_summary`
    """

    return parse_show_ip_bgp_summary(enode(
        'show ip bgp summary'.format(**locals()),
        shell='vtysh'
    ))


def show_ip_bgp_neighbors(enode):
    """
    Show bgp neighbors information.

    This function runs the following vtysh command:

    ::

        # show ip bgp neighbors

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_ip_bgp_neighbors`
    """

    return parse_show_ip_bgp_neighbors(enode(
        'show ip bgp neighbors'.format(**locals()),
        shell='vtysh'
    ))


def show_ip_bgp(enode):
    """
    Show bgp routing information.

    This function runs the following vtysh command:

    ::

        # show ip bgp

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_ip_bgp`
    """

    return parse_show_ip_bgp(enode(
        'show ip bgp'.format(**locals()),
        shell='vtysh'
    ))


__all__ = [
    'ContextManager',
    'Configure',
    'ConfigInterface',
    'ConfigInterfaceVlan',
    'ConfigInterfaceLag',
    'ConfigInterfaceMgmt',
    'ConfigRouterBgp',
    'ConfigVlan',
    'ConfigDhcp',
    'ConfigTftp',
    'show_interface',
    'show_vlan',
    'show_lacp_interface',
    'show_lacp_aggregates',
    'show_lacp_configuration',
    'show_lldp_neighbor_info',
    'show_lldp_statistics',
    'show_ip_bgp_summary',
    'show_ip_bgp_neighbors',
    'show_ip_bgp'
]
