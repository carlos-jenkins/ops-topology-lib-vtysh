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
            'shutdown'.format(**locals()),
            shell='vtysh'
        )

    def no_shutdown(self):
        """
        Disable the VLAN.

        This function runs the following vtysh command:
            # no shutdown

        
        """

        assert not self.enode(
            'no shutdown'.format(**locals()),
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
            'ip address {ipv4}'.format(**locals()),
            shell='vtysh'
        )

    def ipv6_address(self, ipv6):
        """
        Set IP address

        This function runs the following vtysh command:
            # ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        
        """

        assert not self.enode(
            'ipv6 address {ipv6}'.format(**locals()),
            shell='vtysh'
        )

    def routing(self):
        """
        Configure interface as L3.

        This function runs the following vtysh command:
            # routing

        
        """

        assert not self.enode(
            'routing'.format(**locals()),
            shell='vtysh'
        )

    def no_routing(self):
        """
        Unconfigure interface as L3.

        This function runs the following vtysh command:
            # no routing

        
        """

        assert not self.enode(
            'no routing'.format(**locals()),
            shell='vtysh'
        )

    def shutdown(self):
        """
        Enable an interface.

        This function runs the following vtysh command:
            # shutdown

        
        """

        assert not self.enode(
            'shutdown'.format(**locals()),
            shell='vtysh'
        )

    def no_shutdown(self):
        """
        Disable an interface.

        This function runs the following vtysh command:
            # no shutdown

        
        """

        assert not self.enode(
            'no shutdown'.format(**locals()),
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
            'vlan access {vlan_id}'.format(**locals()),
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


__all__ = [
    'ConfigVlan',
    'ConfigInterface',
    'show_interface'
]
