# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016 Hewlett Packard Enterprise Development LP
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
    :return: The parsed result of the show interface command in a \
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
            'ipv4': '20.1.1.2/30'
        }
    """

    show_re = (
        r'\s*Interface (?P<port>\d+) is (?P<interface_state>\S+)\s*'
        r'(\((?P<state_description>.*)\))?\s*'
        r'Admin state is (?P<admin_state>\S+)\s+'
        r'(State information: (?P<state_information>\S+))?\s*'
        r'Hardware: (?P<hardware>\S+), MAC Address: (?P<mac_address>\S+)\s+'
        r'(IPv4 address (?P<ipv4>\S+))?\s*'
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
        if value is not None:
            if value.isdigit():
                result[key] = int(value)
            elif value == 'on':
                result[key] = True
            elif value == 'off':
                result[key] = False
    return result


def parse_show_udld_interface(raw_result):
    """
    Parse the 'show udld interface {intf}' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show udld command in a \
        dictionary of the form:

     ::

        {
            'interface': '1',
            'status': 'Unblock',
            'mode': 'Verify then forward',
            'interval': 3000,
            'retries': 10,
            'port_transition': 0,
            'rx': 0,
            'rx_discard': 0,
            'tx': 0,
        }

    This is the current output of "show udld interface 1":

    switch# show udld interface 1

    Interface 1
     Status: Not running
     Mode: Verify then forward
     Interval: 5000 milliseconds
     Retries: 4
     Port transitions: 0
     RX: 0 valid packets, 0 discarded packets
     TX: 0 packets
    """

    show_re = (
        r'\s*Interface (?P<interface>.*)\n'
        r' Status: (?P<status>.*)\n'
        r' Mode: (?P<mode>.*)\n'
        r' Interval: (?P<interval>\d+) milliseconds\n'
        r' Retries: (?P<retries>\d+)\n'
        r' Port transitions: (?P<port_transition>\d+)\n'
        r' RX: (?P<rx>\d+) valid packets, (?P<rx_discard>\d+) discarded.*\n'
        r' TX: (?P<tx>\d+) packets$'
    )

    re_result = re.match(show_re, raw_result)
    assert re_result

    result = re_result.groupdict()
    for key, value in result.items():
        if value is not None:
            # The interface may be a digit (e.g '1') or string ('fast0/1')
            if value.isdigit() and key != 'interface':
                result[key] = int(value)
    return result


def parse_show_vlan(raw_result):
    """
    Parse the 'show vlan' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show vlan command in a \
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
    :return: The parsed result of the show lacp interface command in a \
        dictionary of the form:

     ::

        {
                'lag_id': '100',
                'local_port_id': '17'
                'remote_port_id': '0'
                'local_port_priority': '1'
                'remote_port_priority': '0'
                'local_key': '100'
                'remote_key': '0'
                'local_state': {
                    'active': True,
                    'short_time': False,
                    'collecting': False,
                    'state_expired': False,
                    'passive': False,
                    'long_timeout': True,
                    'distributing': False,
                    'aggregable': True,
                    'in_sync': False,
                    'neighbor_state': True,
                    'individual': False,
                    'out_sync': True
                },
                'remote_state': {
                    'active': False,
                    'short_time': False,
                    'collecting': False,
                    'state_expired': False,
                    'passive': True,
                    'long_timeout': True,
                    'distributing': False,
                    'aggregable': True,
                    'in_sync': False,
                    'neighbor_state': False,
                    'individual': False,
                    'out_sync': True
                },
                'local_system_id': '70:72:cf:52:54:84',
                'remote_system_id': '00:00:00:00:00:00',
                'local_system_priority': '65534',
                'remote_system_priority': '0'
            }
    """

    lacp_re = (
        r'Aggregate-name\s*:\s*[lag]*(?P<lag_id>\w*)?[\s \S]*'
        r'Port-id\s*\|\s*(?P<local_port_id>\d*)?\s*\|'
        r'\s*(?P<remote_port_id>\d*)?\s+'
        r'Port-priority\s*\|\s*(?P<local_port_priority>\d*)?\s*\|'
        r'\s*(?P<remote_port_priority>\d*)?\s+'
        r'Key\s*\|\s*(?P<local_key>\d*)?\s*\|'
        r'\s*(?P<remote_key>\d*)?\s+'
        r'State\s*\|\s*(?P<local_state>[APFISLNOCDXE]*)?\s*\|'
        r'\s*(?P<remote_state>[APFISLNOCDXE]*)?\s+'
        r'System-id\s*\|\s*'
        r'(?P<local_system_id>([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2})?\s*\|'
        r'\s*(?P<remote_system_id>([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2})?\s+'
        r'System-priority\s*\|\s*(?P<local_system_priority>\d*)?\s*\|'
        r'\s*(?P<remote_system_priority>\d*)?\s+'
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


def parse_show_lacp_aggregates(raw_result):
    """
    Parse the 'show lacp aggregates' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show lacp interface command in a \
        dictionary of the form:

     ::

            {
                'lag1': {
                    'name': 'lag1',
                    'interfaces': [4, 9],
                    'heartbeat_rate': 'slow',
                    'fallback': False,
                    'hash': 'l3-src-dst',
                    'mode': 'off'
                },
                'lag2': {
                    'name': 'lag2',
                    'interfaces': [],
                    'heartbeat_rate': 'slow',
                    'fallback': False,
                    'hash': 'l3-src-dst',
                    'mode': 'off'
                }
            }
    """

    lacp_re = (
        r'Aggregate-name[ ]+: (?P<name>\w+)\s*'
        r'Aggregated-interfaces\s+:[ ]?(?P<interfaces>[\w \-]*)\s*'
        r'Heartbeat rate[ ]+: (?P<heartbeat_rate>slow|fast)\s*'
        r'Fallback[ ]+: (?P<fallback>true|false)\s*'
        r'Hash[ ]+: (?P<hash>l2-src-dst|l3-src-dst)\s*'
        r'Aggregate mode[ ]+: (?P<mode>off|passive|active)\s*'
    )

    result = {}
    for re_result in re.finditer(lacp_re, raw_result):
        lag = re_result.groupdict()
        lag['interfaces'] = lag['interfaces'].split()
        lag['fallback'] = lag['fallback'] == 'True'
        result[lag['name']] = lag

    assert result

    return result


def parse_show_lacp_configuration(raw_result):
    """
    Parse the 'show lacp configuration' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show lacp configuration command in a \
        dictionary of the form:

     ::

            {
                'id': '70:72:cf:af:66:e7',
                'priority': 65534
            }
    """

    configuration_re = (
        r'\s*System-id\s*:\s*(?P<id>\S+)\s*'
        r'System-priority\s*:\s*(?P<priority>\d+)\s*'
    )

    re_result = re.match(configuration_re, raw_result)
    assert re_result

    result = re_result.groupdict()
    result['priority'] = int(result['priority'])
    return result


def parse_show_lldp_neighbor_info(raw_result):
    """
    Parse the 'show lldp neighbor-info' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show lldp neighbor-info command in a \
        dictionary of the form:

     ::

            {
                'port': 1,
                'neighbor_entries': 0,
                'neighbor_entries_deleted': 0,
                'neighbor_entries_dropped': 0,
                'neighbor_entries_age_out': 0,
                'neighbor_chassis_name': None,
                'neighbor_chassis_description': '',
                'neighbor_chassis_id': None,
                'chassis_capabilities_available': '',
                'chassis_capabilities_enabled': '',
                'neighbor_port_id': '',
                'ttl': None
            }
    """

    neighbor_info_re = (
        r'\s*Port\s+:\s*(?P<port>\d+)\s*'
        r'Neighbor entries\s+:\s*(?P<neighbor_entries>\d+)\s*'
        r'Neighbor entries deleted\s+:\s*(?P<neighbor_entries_deleted>\d+)\s*'
        r'Neighbor entries dropped\s+:\s*(?P<neighbor_entries_dropped>\d+)\s*'
        r'Neighbor entries age-out\s+:\s*(?P<neighbor_entries_age_out>\d+)\s*'
        r'Neighbor Chassis-Name\s+:\s*(?P<neighbor_chassis_name>\S+)?\s*'
        r'Neighbor Chassis-Description\s+:\s*'
        r'(?P<neighbor_chassis_description>.*)\s*'
        r'Neighbor Chassis-ID\s+:\s*(?P<neighbor_chassis_id>[0-9a-f:]+)?\s*'
        r'Chassis Capabilities Available\s*:\s*'
        r'(?P<chassis_capabilities_available>.*)?\s*'
        r'Chassis Capabilities Enabled\s*:\s*'
        r'(?P<chassis_capabilities_enabled>.*)?\s*'
        r'Neighbor Port-ID\s*:\s*(?P<neighbor_port_id>.*)?\s*'
        r'TTL\s+:\s*(?P<ttl>\d+)?\s*'
    )

    re_result = re.match(neighbor_info_re, raw_result)
    assert re_result

    result = re_result.groupdict()
    for key, value in result.items():
        if value and value.isdigit():
            result[key] = int(value)
    return result


def parse_show_lldp_statistics(raw_result):
    """
    Parse the 'show lldp statistics' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show lldp statistics command in a \
        dictionary of the form:

     ::

            {
                'total_packets_transmited': 0,
                'total_packets_received': 0,
                'total_packets_received_and_discarded': 0,
                'total_tlvs_unrecognized': 0
            }
    """

    neighbor_info_re = (
        r'\s*Total\sPackets\stransmitted\s*:\s*'
        r'(?P<total_packets_transmited>\d+)\s*'
        r'Total\sPackets\sreceived\s*:\s*(?P<total_packets_received>\d+)\s*'
        r'Total\sPacket\sreceived\sand\sdiscarded\s*:\s*'
        r'(?P<total_packets_received_and_discarded>\d+)\s*'
        r'Total\sTLVs\sunrecognized\s*:\s*(?P<total_tlvs_unrecognized>\d+)\s*'

    )

    re_result = re.match(neighbor_info_re, raw_result)
    assert re_result

    result = re_result.groupdict()
    for key, value in result.items():
        if value and value.isdigit():
            result[key] = int(value)

    return result


def parse_show_ip_bgp_summary(raw_result):
    """
    Parse the 'show ip bgp summary' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show ip bgp summary command in a \
        dictionary of the form:

     ::

        {
            'bgp_router_identifier': '1.0.0.1',
            'local_as_number': 64000,
            'rib_entries': 15,
            'peers': 2,
            '20.1.1.1': { 'AS': 65000,
                   'msgrcvd': 83,
                   'msgsent': 86,
                   'up_down': '01:19:21',
                   'state': 'Established',
                   'neighbor': '20.1.1.1'
             },
            '20.1.1.2': { 'AS': 65000,
                   'msgrcvd': 100,
                   'msgsent': 105,
                   'up_down': '01:22:22',
                   'state': 'Established',
                   'neighbor': '20.1.1.2'
            }
        }
    """

    local_bgp_re = (
        r'BGP router identifier (?P<bgp_router_identifier>[^,]+), '
        r'local AS number (?P<local_as_number>\d+)\nRIB entries '
        r'(?P<rib_entries>\d+)\nPeers (?P<peers>\d+)\n\n'
    )

    summary_re = (
        r'(?P<neighbor>\S+)\s+(?P<as_number>\d+)\s+(?P<msgrcvd>\d+)\s+'
        r'(?P<msgsent>\d+)\s+(?P<up_down>\S+)\s+(?P<state>\w+)\s*'
    )

    result = {}
    re_result = re.match(local_bgp_re, raw_result)
    assert re_result
    result = re_result.groupdict()
    for key, value in result.items():
        if value and value.isdigit():
            result[key] = int(value)

    for line in raw_result.splitlines():
        re_result = re.search(summary_re, line)
        if re_result:
            partial = re_result.groupdict()
            for key, value in partial.items():
                if value and value.isdigit():
                    partial[key] = int(value)
            result[partial['neighbor']] = partial

    return result


def parse_show_ip_bgp_neighbors(raw_result):
    """
    Parse the 'show ip bgp neighbor' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show ip bgp neighbor command in a \
        dictionary of the form:

     ::

        {
            '20.1.1.1': { 'name': '20.1.1.1',
                   'remote_as': 65000,
                   'state': 'Established',
                   'tcp_port_number': 179 ,
                   'bgp_peer_dropped_count': 0,
                   'bgp_peer_dynamic_cap_in_count': 0,
                   'bgp_peer_dynamic_cap_out_count': 0,
                   'bgp_peer_established_count': 1,
                   'bgp_peer_keepalive_in_count': 2,
                   'bgp_peer_keepalive_out_count': 3,
                   'bgp_peer_notify_in_count': 0,
                   'bgp_peer_notify_out_count': 0,
                   'bgp_peer_open_in_count': 0,
                   'bgp_peer_open_out_coun': 1,
                   'bgp_peer_readtime': 249,
                   'bgp_peer_refresh_in_count': 0,
                   'bgp_peer_refresh_out_count': 0,
                   'bgp_peer_resettime': 127,
                   'bgp_peer_update_in_count': 2,
                   'bgp_peer_update_out_count': 2,
                   'bgp_peer_uptime': 189

             },
            '20.1.1.10': { 'name': '20.1.1.10',
                   'remote_as': 65000,
                   'state': 'Established',
                   'tcp_port_number': 179 ,
                   'bgp_peer_dropped_count': 0,
                   'bgp_peer_dynamic_cap_in_count': 0,
                   'bgp_peer_dynamic_cap_out_count': 0,
                   'bgp_peer_established_count': 1,
                   'bgp_peer_keepalive_in_count': 2,
                   'bgp_peer_keepalive_out_count': 3,
                   'bgp_peer_notify_in_count': 0,
                   'bgp_peer_notify_out_count': 0,
                   'bgp_peer_open_in_count': 0,
                   'bgp_peer_open_out_coun': 1,
                   'bgp_peer_readtime': 281,
                   'bgp_peer_refresh_in_count': 0,
                   'bgp_peer_refresh_out_count': 0,
                   'bgp_peer_resettime': 127,
                   'bgp_peer_update_in_count': 2,
                   'bgp_peer_update_out_count': 4,
                   'bgp_peer_uptime': 221

             }
    """

    neighbor_re = (
        r'\s*name: (?P<name>[^,]+), remote-as: (?P<remote_as>\d+)\s+state: '
        r'(?P<state>\w+)\s*tcp_port_number: (?P<tcp_port_number>\d+)'
        r'\s*statistics:\s*bgp_peer_dropped_count: '
        r'(?P<bgp_peer_dropped_count>\d+)\s*bgp_peer_dynamic_cap_in_count: '
        r'(?P<bgp_peer_dynamic_cap_in_count>\d+)'
        r'\s*bgp_peer_dynamic_cap_out_count: '
        r'(?P<bgp_peer_dynamic_cap_out_count>\d+)'
        r'\s*bgp_peer_established_count: (?P<bgp_peer_established_count>\d+)'
        r'\s*bgp_peer_keepalive_in_count: '
        r'(?P<bgp_peer_keepalive_in_count>\d+)'
        r'\s*bgp_peer_keepalive_out_count: '
        r'(?P<bgp_peer_keepalive_out_count>\d+)\s*bgp_peer_notify_in_count: '
        r'(?P<bgp_peer_notify_in_count>\d+)\s*bgp_peer_notify_out_count: '
        r'(?P<bgp_peer_notify_out_count>\d+)\s*bgp_peer_open_in_count: '
        r'(?P<bgp_peer_open_in_count>\d+)\s*bgp_peer_open_out_count: '
        r'(?P<bgp_peer_open_out_count>\d+)\s*bgp_peer_readtime: '
        r'(?P<bgp_peer_readtime>\d+)\s*bgp_peer_refresh_in_count: '
        r'(?P<bgp_peer_refresh_in_count>\d+)\s*bgp_peer_refresh_out_count: '
        r'(?P<bgp_peer_refresh_out_count>\d+)\s*bgp_peer_resettime: '
        r'(?P<bgp_peer_resettime>\d+)\s*bgp_peer_update_in_count: '
        r'(?P<bgp_peer_update_in_count>\d+)\s*bgp_peer_update_out_count: '
        r'(?P<bgp_peer_update_out_count>\d+)\s*bgp_peer_uptime: '
        r'(?P<bgp_peer_uptime>\d+)\s*'
    )

    result = {}
    for re_result in re.finditer(neighbor_re, raw_result):
        partial = re_result.groupdict()
        for key, value in partial.items():
            if value and value.isdigit():
                partial[key] = int(value)
        result[partial['name']] = partial

    return result


def parse_show_ip_bgp(raw_result):
    """
    Parse the 'show ip bgp' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show ip bgp command in a \
        list of dictionaries of the form:

     ::

        [
            {
                'route_status': '*>',
                'network': '10.2.0.2/32',
                'next_hop': '20.1.1.1',
                'metric': 0,
                'locprf': 0,
                'weight': 0,
                'path': '65000 64100 i'
            },
            {
                'route_status': '*',
                'network': '10.2.0.2/32',
                'next_hop': '20.1.1.10',
                'metric': 0,
                'locprf': 0,
                'weight': 0,
                'path': '65000 64100 i'
            }
        ]
    """

    routes_re = (
        r'(?P<route_status>[*>sdh=iSR]+)\s+(?P<network>\S+)\s+'
        r'(?P<next_hop>\S+)\s+(?P<metric>\d+)\s+(?P<locprf>\d+)\s+'
        r'(?P<weight>\d+)\s+(?P<path>.*)\w?\s*'
    )

    result = []
    for line in raw_result.splitlines():
        re_result = re.search(routes_re, line)
        if re_result:
            partial = re_result.groupdict()
            for key, value in partial.items():
                if value and value.isdigit():
                    partial[key] = int(value)
            result.append(partial)

    return result


def parse_show_ipv6_bgp(raw_result):
    """
    Parse the 'show ipv6 bgp' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show ipv6 bgp command in a \
        list of dictionaries of the form:

     ::

        [
            {
                'route_status': '*>',
                'network': '10::/126',
                'next_hop': '::',
                'metric': 0,
                'locprf': 0,
                'weight': 0,
                'path': '65000 64100 i'
            },
            {
                'route_status': '*',
                'network': '10::/126',
                'next_hop': '3::1',
                'metric': 0,
                'locprf': 0,
                'weight': 0,
                'path': '65000 64100 i'
            }
        ]
    """

    routes_re = (
        r'(?P<route_status>[*>sdh=iSR]+)\s+(?P<network>\S+)\s+'
        r'(?P<next_hop>\S+)\s+(?P<metric>\d+)\s+(?P<locprf>\d+)\s+'
        r'(?P<weight>\d+)\s+(?P<path>.*)\w?\s*'
    )

    result = []
    for line in raw_result.splitlines():
        re_result = re.search(routes_re, line)
        if re_result:
            partial = re_result.groupdict()
            for key, value in partial.items():
                if value and value.isdigit():
                    partial[key] = int(value)
            result.append(partial)

    return result


def parse_ping_repetitions(raw_result):
    """
    Parse the 'ping' command raw output.

    :param str raw_result: ping raw result string.
    :rtype: dict
    :return: The parsed result of the ping command in a \
        list of dictionaries of the form:

     ::

        {
            'transmitted': 0,
            'received': 0,
            'errors': 0,
            'packet_loss': 0
        }
    """

    ping_re = (
        r'^(?P<transmitted>\d+) packets transmitted, '
        r'(?P<received>\d+) packets received,'
        r'( \+(?P<errors>\d+) errors,)? '
        r'(?P<packet_loss>\d+)% packet loss$'
    )

    result = {}
    for line in raw_result.splitlines():
        re_result = re.search(ping_re, line)
        if re_result:
            for key, value in re_result.groupdict().items():
                if value is None:
                    result[key] = 0
                elif value.isdigit():
                    result[key] = int(value)

    return result


def parse_ping6_repetitions(raw_result):
    """
    Parse the 'ping6' command raw output.

    :param str raw_result: ping6 raw result string.
    :rtype: dict
    :return: The parsed result of the ping6 command in a \
        list of dictionaries of the form:

     ::

        {
            'transmitted': 0,
            'received': 0,
            'errors': 0,
            'packet_loss': 0
        }
    """

    ping_re = (
        r'^(?P<transmitted>\d+) packets transmitted, '
        r'(?P<received>\d+) packets received,'
        r'( \+(?P<errors>\d+) errors,)? '
        r'(?P<packet_loss>\d+)% packet loss$'
    )

    result = {}
    for line in raw_result.splitlines():
        re_result = re.search(ping_re, line)
        if re_result:
            for key, value in re_result.groupdict().items():
                if value is None:
                    result[key] = 0
                elif value.isdigit():
                    result[key] = int(value)

    return result


def parse_show_rib(raw_result):
    """
    Parse the 'show rib' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show rib command in a \
        dictionary of the form:

     ::

        {
            'ipv4_entries': [
                {
                    'id': '140.0.0.0',
                    'prefix': '30',
                    'selected': True,
                    'next_hops': [
                        {
                            'selected': True,
                            'via': '10.10.0.2',
                            'distance': '20',
                            'from': 'BGP',
                            'metric': '0'
                        }
                    ]
                },
                {
                    'id': '193.0.0.2',
                    'prefix': '32',
                    'selected': True,
                    'next_hops': [
                        {
                            'selected': True,
                            'via': '50.0.0.2',
                            'distance': '1',
                            'from': 'static',
                            'metric': '0'
                        },
                        {
                            'selected': True,
                            'via': '56.0.0.3',
                            'distance': '1',
                            'from': 'static',
                            'metric': '0'
                        }
                    ]
                },
                {
                    'id': '10.10.0.0',
                    'prefix': '24',
                    'selected': True,
                    'next_hops': [
                        {
                            'selected': True,
                            'via': '1',
                            'distance': '0',
                            'from': 'connected',
                            'metric': '0'
                        }
                    ]
                }
            ],
            'ipv6_entries': [
                {
                    'id': '2002::/64',
                    'selected': True,
                    'next_hops': [
                        {
                            'selected': True,
                            'via': '4',
                            'distance': '0',
                            'from': 'connected',
                            'metric': '0'
                        }
                    ]
                },
                {
                    'id': '2010:bd9::/32',
                    'selected': True,
                    'next_hops': [
                        {
                            'selected': True,
                            'via': '2005::2',
                            'distance': '1',
                            'from': 'static',
                            'metric': '0'
                        },
                        {
                            'selected': True,
                            'via': '2001::2',
                            'distance': '1',
                            'from': 'static',
                            'metric': '0'
                        },
                        {
                            'selected': False,
                            'via': '2002::2',
                            'distance': '1',
                            'from': 'static',
                            'metric': '0'
                        }
                    ]
                }
            ]
        }
    """

    ipv4_entries_re = (
        r'ipv4 rib entries'
    )

    ipv6_entries_re = (
        r'ipv6 rib entries'
    )

    ipv4_network_re = (
        r'(?P<selected>\*?)(?P<network>\d+\.\d+\.\d+\.\d+)/(?P<prefix>\d+)'
    )

    ipv6_network_re = (
        r'(?P<selected>\*?)'
        r'(?P<network>(?:(?:(?:[0-9A-Za-z]+:)+:?([0-9A-Za-z]+)?)+)/\d+)'
    )

    ipv4_nexthop_re = (
        r'(?P<selected>\*?)via\s+(?P<via>(?:\d+\.\d+\.\d+\.\d+|\d+)),\s+'
        r'\[(?P<distance>\d+)/(?P<metric>\d+)\],\s+(?P<from>\S+)'
    )

    ipv6_nexthop_re = (
        r'(?P<selected>\*?)'
        r'via\s+(?P<via>(?:(?:(?:[0-9A-Za-z]+:)+:?([0-9A-Za-z]+)?)+|\d+)),\s+'
        r'\[(?P<distance>\d+)/(?P<metric>\d+)\],\s+(?P<from>\S+)'
    )

    result = {}
    result['ipv4_entries'] = []
    result['ipv6_entries'] = []

    lines = raw_result.splitlines()
    line_index = 0

    while line_index < len(lines):
        if re.search(ipv4_entries_re, lines[line_index]):

            check_for_ipv4_entries = False

            while (not check_for_ipv4_entries and line_index < len(lines)):
                if re.search(ipv4_network_re, lines[line_index]):
                    check_for_ipv4_entries = True
                else:
                    line_index += 1

            while (check_for_ipv4_entries and line_index < len(lines)):
                re_result = re.search(ipv4_network_re, lines[line_index])

                if re_result:
                    network = {}
                    partial = re_result.groupdict()

                    if partial['selected'] == '*':
                        network['selected'] = True
                    else:
                        network['selected'] = False

                    network['id'] = partial['network']
                    network['prefix'] = partial['prefix']

                    network['next_hops'] = []
                    check_for_next_hops = True

                    line_index += 1

                    while (check_for_next_hops and line_index < len(lines)):
                        re_result = re.search(
                            ipv4_nexthop_re,
                            lines[line_index]
                            )

                        if re_result:
                            partial = re_result.groupdict()

                            if partial['selected'] == '*':
                                partial['selected'] = True
                            else:
                                partial['selected'] = False

                            network['next_hops'].append(partial)
                            line_index += 1
                        else:
                            check_for_next_hops = False

                    result['ipv4_entries'].append(network)
                else:
                    check_for_ipv4_entries = False

        if re.search(ipv6_entries_re, lines[line_index]):
            check_for_ipv6_entries = False

            while (not check_for_ipv6_entries and line_index < len(lines)):
                if re.search(ipv6_network_re, lines[line_index]):
                    check_for_ipv6_entries = True
                else:
                    line_index += 1

            while (check_for_ipv6_entries and line_index < len(lines)):
                re_result = re.search(ipv6_network_re, lines[line_index])

                if re_result:
                    network = {}
                    partial = re_result.groupdict()

                    if partial['selected'] == '*':
                        network['selected'] = True
                    else:
                        network['selected'] = False

                    network['id'] = partial['network']

                    network['next_hops'] = []
                    check_for_next_hops = True

                    line_index += 1

                    while (check_for_next_hops and line_index < len(lines)):
                        re_result = re.search(
                            ipv6_nexthop_re,
                            lines[line_index]
                            )

                        if re_result:
                            partial = re_result.groupdict()

                            if partial['selected'] == '*':
                                partial['selected'] = True
                            else:
                                partial['selected'] = False

                            network['next_hops'].append(partial)
                            line_index += 1
                        else:
                            check_for_next_hops = False

                    result['ipv6_entries'].append(network)
                else:
                    check_for_ipv6_entries = False

        line_index += 1

    return result


def parse_show_running_config(raw_result):
    """
    Parse the 'show running-config' command raw output.
    This parser currently returns only BGP section of the show-running
    command, please review the doc/developer.rst file to get more information
    on adding new sections.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show vlan command in a
              dictionary of the form:

     ::

         {
            'bgp':
                {'64001':
                    {'networks': ['10.240.1.2/32',
                                '10.240.10.2/32',
                                '10.240.9.2/32'],
                    'router_id': '2.0.0.1'},
                '64002':
                    {'networks': ['11.240.1.2/32',
                                '11.240.10.2/32',
                                '11.240.9.2/32'],
                    'router_id': '3.0.0.1'}
                }
        }
    """

    result = {}

    # Only the bgp section is captured
    bgp_section_re = r'router bgp.*(?=!)'
    re_bgp_section = re.findall(bgp_section_re, raw_result, re.DOTALL)
    as_number_re = r'router bgp\s+(\d+)'
    router_id_re = r'\s+bgp router-id\s+(.*)'
    network_re = r'\s+network\s+(.*)'
    re_as_number = None
    result['bgp'] = {}
    if re_bgp_section:
        for line in re_bgp_section[0].splitlines():
            re_result = re.match(as_number_re, line)
            if re_result:
                re_as_number = re_result.group(1)
                result['bgp'][re_as_number] = {}

            re_result = re.match(router_id_re, line)
            if re_result:
                result['bgp'][re_as_number]['router_id'] = re_result.group(1)

            re_result = re.match(network_re, line)
            if re_result:
                network = re_result.group(1)
                if 'networks' not in result['bgp'][re_as_number].keys():
                    result['bgp'][re_as_number]['networks'] = []
                    result['bgp'][re_as_number]['networks'].append(network)
                else:
                    result['bgp'][re_as_number]['networks'].append(network)

    return result


def parse_show_ip_route(raw_result):
    """
    Parse the 'show ip route' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: list
    :return: The parsed result of the show ip route command in a \
        list of dictionaries of the form:

     ::

        [
            {
                'id': '140.0.0.0',
                'prefix': '30',
                'next_hops': [
                    {
                        'via': '10.10.0.2',
                        'distance': '20',
                        'from': 'bgp',
                        'metric': '0'
                    }
                ]
            },
            {
                'id': '10.10.0.0',
                'prefix': '24',
                'next_hops': [
                    {
                        'via': '1',
                        'distance': '0',
                        'from': 'connected',
                        'metric': '0'
                    }
                ]
            },
            {
                'id': '193.0.0.2',
                'prefix': '32',
                'next_hops': [
                    {
                        'via': '50.0.0.2',
                        'distance': '1',
                        'from': 'static',
                        'metric': '0'
                    },
                    {
                        'via': '56.0.0.3',
                        'distance': '1',
                        'from': 'static',
                        'metric': '0'
                    }
                ]
            }
        ]
    """

    ipv4_network_re = (
        r'(?P<network>\d+\.\d+\.\d+\.\d+)/(?P<prefix>\d+)'
    )

    ipv4_nexthop_re = (
        r'via\s+(?P<via>(?:\d+\.\d+\.\d+\.\d+|\d+)),\s+'
        r'\[(?P<distance>\d+)/(?P<metric>\d+)\],\s+(?P<from>\S+)'
    )

    result = []

    lines = raw_result.splitlines()
    line_index = 0

    while line_index < len(lines):
        re_result = re.search(ipv4_network_re, lines[line_index])

        if re_result:
            network = {}
            partial = re_result.groupdict()

            network['id'] = partial['network']
            network['prefix'] = partial['prefix']

            network['next_hops'] = []
            check_for_next_hops = True

            line_index += 1

            while (check_for_next_hops and line_index < len(lines)):
                re_result = re.search(
                    ipv4_nexthop_re,
                    lines[line_index]
                    )

                if re_result:
                    partial = re_result.groupdict()

                    network['next_hops'].append(partial)
                    line_index += 1
                else:
                    check_for_next_hops = False

            result.append(network)
        else:
            line_index += 1

    return result


def parse_show_ip_ecmp(raw_result):
    """
    Parse the 'show ip ecmp' command raw output.

    :param str raw_result: vtysh raw result string.
    :rtype: dict
    :return: The parsed result of the show ip ecmp in a \
        dictionary of the form:

    ::

        {
            'global_status': True,
            'resilient': False,
            'src_ip': True,
            'dest_ip': True,
            'src_port': True,
            'dest_port': True
        }
    """

    show_ip_ecmp_re = (
        r'\s*ECMP Configuration\s*-*\s*'
        r'ECMP Status\s*: (?P<global_status>\S+)\s*'
        r'(Resilient Hashing\s*: (?P<resilient>\S+))?\s*'
        r'ECMP Load Balancing by\s*-*\s*'
        r'Source IP\s*: (?P<src_ip>\S+)\s*'
        r'Destination IP\s*: (?P<dest_ip>\S+)\s*'
        r'Source Port\s*: (?P<src_port>\S+)\s*'
        r'Destination Port\s*: (?P<dest_port>\S+)\s*'
    )

    re_result = re.match(show_ip_ecmp_re, raw_result)
    assert re_result

    result = re_result.groupdict()
    for key, value in result.items():
        if value is not None:
            if value == 'Enabled':
                result[key] = True
            elif value == 'Disabled':
                result[key] = False

    return result

__all__ = [
    'parse_show_vlan', 'parse_show_lacp_aggregates',
    'parse_show_lacp_interface', 'parse_show_interface',
    'parse_show_lacp_configuration', 'parse_show_lldp_neighbor_info',
    'parse_show_lldp_statistics', 'parse_show_ip_bgp_summary',
    'parse_show_ip_bgp_neighbors', 'parse_show_ip_bgp',
    'parse_show_udld_interface', 'parse_ping_repetitions',
    'parse_ping6_repetitions', 'parse_show_rib',
    'parse_show_running_config', 'parse_show_ip_route', 'parse_show_ipv6_bgp',
    'parse_show_ip_ecmp'

]
