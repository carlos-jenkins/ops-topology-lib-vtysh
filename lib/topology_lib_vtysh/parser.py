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

"""
Parse vtysh commands with output to a python dictionary.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division


import re


def parse_show_interface(raw_result):
    """
    Parse the 'show interface' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show interface command in a
    dictionary of the form:

     ::

        {
            'admin_state': 'down',
            'autonegotiation': True,
            'conection_type': 'Half-duplex',
            'hardware': 'Ethernet',
            'input_flow_control': False,
            'interface_state': 'down',
            'mac_address': '70:72:cf:d7:d3:dd',
            'mtu': 0,
            'output_flow_control': False,
            'port': 7,
            'rx_crc_fcs': 0,
            'rx_dropped': 0,
            'rx_bytes': 0,
            'rx_error': 0,
            'rx_packets': 0,
            'speed': 0,
            'speed_unit': 'Mb/s',
            'state_description': 'Administratively down',
            'state_information': 'admin_down',
            'tx_bytes': 0,
            'tx_collisions': 0,
            'tx_dropped': 0,
            'tx_errors': 0,
            'tx_packets': 0
        }
    """

    show_re = (
        r'\s+Interface (?P<port>\d+) is (?P<interface_state>\S+) '
        r'\((?P<state_description>.*)\)\s+'
        r'Admin state is (?P<admin_state>\S+)\s+'
        r'State information: (?P<state_information>\S+)\s+'
        r'Hardware: (?P<hardware>\S+), MAC Address: (?P<mac_address>\S+)\s+'
        r'MTU (?P<mtu>\d+)\s+'
        r'(?P<conection_type>\S+)\s+'
        r'Speed (?P<speed>\d+) (?P<speed_unit>\S+)\s+'
        r'Auto-Negotiation is turned (?P<autonegotiation>\S+)\s+'
        r'Input flow-control is (?P<input_flow_control>\w+),\s+'
        r'output flow-control is (?P<output_flow_control>\w+)\s+'
        r'RX\s+'
        r'(?P<rx_packets>\d+) input packets\s+'
        r'(?P<rx_bytes>\d+) bytes\s+'
        r'(?P<rx_error>\d+) input error\s+'
        r'(?P<rx_dropped>\d+) dropped\s+'
        r'(?P<rx_crc_fcs>\d+) CRC/FCS\s+'
        r'TX\s+'
        r'(?P<tx_packets>\d+) output packets\s+'
        r'(?P<tx_bytes>\d+) bytes\s+'
        r'(?P<tx_errors>\d+) input error\s+'
        r'(?P<tx_dropped>\d+) dropped\s+'
        r'(?P<tx_collisions>\d+) collision'
    )

    re_result = re.match(show_re, raw_result)
    assert re_result

    result = re_result.groupdict()
    for key, value in result.items():
        if value.isdigit():
            result[key] = int(value)
        elif value == 'on':
            result[key] = True
        elif value == 'off':
            result[key] = False
    return result


def parse_show_vlan(raw_result):
    """
    Parse the 'show vlan' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show vlan command in a
    dictionary of the form:

     ::

        {
            '1': { 'name': 'vlan1',
                   'ports': [''],
                   'reason': 'admin_down',
                   'reserved': None,
                   'status': 'down',
                   'vlan_id': '1'
             },
             '2': {
                    'name': 'vlan2',
                    'ports': ['7', '3', '8', 'vlan2', '1'],
                    'reason': 'ok',
                    'reserved': None,
                    'status': 'up',
                    'vlan_id': '2'
            }
        }
    """

    vlan_re = (
        r'(?P<vlan_id>\d+)\s+(?P<name>\S+)\s+(?P<status>\S+)\s+'
        r'(?P<reason>\S+)\s*(?P<reserved>\(\w+\))?\s*(?P<ports>[\w ,]*)'
    )

    result = {}
    for line in raw_result.splitlines():
        re_result = re.search(vlan_re, line)
        if re_result:
            partial = re_result.groupdict()
            partial['ports'] = partial['ports'].split(', ')
            result[partial['vlan_id']] = partial

    return result


def parse_show_lacp_interface(raw_result):
    """
    Parse the 'show lacp interface' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show lacp interface command in a
    dictionary of the form:

     ::

        {
                'lag_id': '1',
                'local_system_id': '',
                'remote_system_id': '',
                'local_port_id': '',
                'remote_port_id': '',
                'local_key': '',
                'remote_key': '',
                'local_state': {
                    'active': False,
                    'short_time': False,
                    'collecting': True,
                    'state_expired': False,
                    'passive': False,
                    'long_timeout': False,
                    'distributing': True,
                    'aggregable': False,
                    'in_sync': False,
                    'neighbor_state': False,
                    'individual': False,
                    'out_sync': False
                },
                'remote_state': {
                    'active': False,
                    'short_time': False,
                    'collecting': True,
                    'state_expired': False,
                    'passive': False,
                    'long_timeout': False,
                    'distributing': False,
                    'aggregable': False,
                    'in_sync': True,
                    'neighbor_state': False,
                    'individual': False,
                    'out_sync': False
                },
            }
    """

    lacp_re = (
        r'Aggregate-name\s*:\s*[lag]*(?P<lag_id>\w*)?[\s \S]*'
        r'System-id\s*\|\s*(?P<local_system_id>.*)?\|'
        r'\s*(?P<remote_system_id>.*)?\s+'
        r'Port-id\s*\|\s*(?P<local_port_id>.*)?\|\s*(?P<remote_port_id>.*)?\s+'
        r'Key\s*\|\s*(?P<local_key>.*)?\|\s*(?P<remote_key>.*)?\s+'
        r'State\s*\|\s*(?P<local_state>.*)?\|\s*(?P<remote_state>.*)?\s+'
    )

    re_result = re.search(lacp_re, raw_result)
    assert re_result

    result = re_result.groupdict()

    for state in ['local_state', 'remote_state']:
        tmp_dict = {
            'active': 'A' in result[state],
            'short_time': 'S' in result[state],
            'collecting': 'C' in result[state],
            'state_expired': 'X' in result[state],
            'passive': 'P' in result[state],
            'long_timeout': 'L' in result[state],
            'distributing': 'D' in result[state],
            'aggregable': 'F' in result[state],
            'in_sync': 'N' in result[state],
            'neighbor_state': 'E' in result[state],
            'individual': 'I' in result[state],
            'out_sync': 'O' in result[state]
        }

        result[state] = tmp_dict

    return result
