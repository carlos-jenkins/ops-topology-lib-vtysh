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
OpenSwitch Test for vtysh related commands.
"""

from __future__ import unicode_literals

from deepdiff import DeepDiff

from topology_lib_vtysh.parser import (parse_show_interface,
                                       parse_show_vlan,
                                       parse_show_lacp_interface,
                                       parse_show_lacp_aggregates,
                                       parse_show_lacp_configuration,
                                       parse_show_lldp_neighbor_info,
                                       parse_show_lldp_statistics,
                                       parse_show_ip_bgp_summary,
                                       parse_show_ip_bgp_neighbors,
                                       parse_show_ip_bgp,
                                       parse_show_ip_route,
                                       parse_show_rib,
                                       parse_ping_repetitions,
                                       parse_ping6_repetitions,
                                       parse_show_running_config
                                       )


def test_parse_show_vlan():
    raw_result = """\

--------------------------------------------------------------------------------
VLAN    Name      Status   Reason         Reserved       Ports
--------------------------------------------------------------------------------
2       vlan2     up       ok                            7, 3, 8, vlan2, 1
1       vlan1     down     admin_down
    """

    result = parse_show_vlan(raw_result)

    expected = {
        '1': {
            'name': 'vlan1',
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

    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_show_interface():
    raw_result = """\

Interface 7 is down (Administratively down)
 Admin state is down
 State information: admin_down
 Hardware: Ethernet, MAC Address: 70:72:cf:d7:d3:dd
 MTU 0
 Half-duplex
 Speed 0 Mb/s
 Auto-Negotiation is turned on
 Input flow-control is off, output flow-control is off
 RX
            0 input packets              0 bytes
            0 input error                0 dropped
            0 CRC/FCS
 TX
            0 output packets             0 bytes
            0 input error                0 dropped
            0 collision

    """

    result = parse_show_interface(raw_result)

    expected = {
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
        'tx_packets': 0,
        'ipv4': None

    }

    ddiff = DeepDiff(result, expected)
    assert not ddiff

    raw_result2 = """\

Interface 1 is up
 Admin state is up
 Hardware: Ethernet, MAC Address: 70:72:cf:75:25:70
 IPv4 address 20.1.1.2/30
 MTU 0
 Full-duplex
 Speed 1000 Mb/s
 Auto-Negotiation is turned on
 Input flow-control is off, output flow-control is off
 RX
            0 input packets              0 bytes
            0 input error                0 dropped
            0 CRC/FCS
 TX
            0 output packets             0 bytes
            0 input error                0 dropped
            0 collision
    """

    result2 = parse_show_interface(raw_result2)

    expected2 = {
        'admin_state': 'up',
        'autonegotiation': True,
        'conection_type': 'Full-duplex',
        'hardware': 'Ethernet',
        'input_flow_control': False,
        'interface_state': 'up',
        'mac_address': '70:72:cf:75:25:70',
        'mtu': 0,
        'output_flow_control': False,
        'port': 1,
        'rx_crc_fcs': 0,
        'rx_dropped': 0,
        'rx_bytes': 0,
        'rx_error': 0,
        'rx_packets': 0,
        'speed': 1000,
        'speed_unit': 'Mb/s',
        'state_description': None,
        'state_information': None,
        'tx_bytes': 0,
        'tx_collisions': 0,
        'tx_dropped': 0,
        'tx_errors': 0,
        'tx_packets': 0,
        'ipv4': '20.1.1.2/30'
    }

    ddiff2 = DeepDiff(result2, expected2)
    assert not ddiff2


def test_parse_show_lacp_interface():
    raw_result = """\
State abbreviations :
A - Active        P - Passive      F - Aggregable I - Individual
S - Short-timeout L - Long-timeout N - InSync     O - OutofSync
C - Collecting    D - Distributing
X - State m/c expired              E - Default neighbor state


Aggregate-name : lag100
-------------------------------------------------
                       Actor             Partner
-------------------------------------------------
Port-id            | 17                 | 0
Port-priority      | 1                  | 0
Key                | 100                | 0
State              | ALFOE              | PLFO
System-id          | 70:72:cf:52:54:84  | 00:00:00:00:00:00
System-priority    | 65534              | 0
"""

    result = parse_show_lacp_interface(raw_result)

    expected = {
        'lag_id': '100',
        'local_port_id': '17',
        'remote_port_id': '0',
        'local_port_priority': '1',
        'remote_port_priority': '0',
        'local_key': '100',
        'remote_key': '0',
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

    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_show_lacp_aggregates():
    raw_result = """\
Aggregate-name        : lag1
Aggregated-interfaces : 4 9
Heartbeat rate        : slow
Fallback              : false
Hash                  : l3-src-dst
Aggregate mode        : off


Aggregate-name        : lag2
Aggregated-interfaces :
Heartbeat rate        : slow
Fallback              : false
Hash                  : l3-src-dst
Aggregate mode        : off
    """

    result = parse_show_lacp_aggregates(raw_result)

    expected = {
        'lag1': {
            'name': 'lag1',
            'interfaces': ['4', '9'],
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
        },
    }

    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_show_lacp_configuration():
    raw_result = """\
System-id       : 70:72:cf:af:66:e7
System-priority : 65534
    """

    result = parse_show_lacp_configuration(raw_result)

    expected = {
        'id': '70:72:cf:af:66:e7',
        'priority': 65534
    }

    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_show_lldp_neighbor_info():
    raw_result = """\
Port                           : 1
Neighbor entries               : 0
Neighbor entries deleted       : 0
Neighbor entries dropped       : 0
Neighbor entries age-out       : 0
Neighbor Chassis-Name          :
Neighbor Chassis-Description   :
Neighbor Chassis-ID            :
Chassis Capabilities Available :
Chassis Capabilities Enabled   :
Neighbor Port-ID               :
TTL                            :
    """

    result = parse_show_lldp_neighbor_info(raw_result)

    expected = {
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
    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_show_lldp_statistics():
    raw_result = """\
Total Packets transmitted : 0
Total Packets received : 0
Total Packet received and discarded : 0
Total TLVs unrecognized : 0
    """

    result = parse_show_lldp_statistics(raw_result)

    expected = {
        'total_packets_transmited': 0,
        'total_packets_received': 0,
        'total_packets_received_and_discarded': 0,
        'total_tlvs_unrecognized': 0
    }
    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_show_ip_bgp_summary():
    raw_result = """\
BGP router identifier 2.0.0.1, local AS number 64000
RIB entries 5
Peers 3

Neighbor             AS MsgRcvd MsgSent Up/Down  State
192.168.1.10      64000       0       0 never           Idle
20.1.1.1          65000       0       0 never         Active
20.1.1.10         65000       0       0 never         Active
    """

    result = parse_show_ip_bgp_summary(raw_result)

    expected = {
        'bgp_router_identifier': '2.0.0.1',
        '20.1.1.1': {
            'up_down': 'never',
            'state': 'Active',
            'msgsent': 0,
            'neighbor': '20.1.1.1',
            'as_number': 65000,
            'msgrcvd': 0
        },
        'rib_entries': 5,
        'peers': 3,
        '192.168.1.10': {
            'up_down': 'never',
            'state': 'Idle',
            'msgsent': 0,
            'neighbor': '192.168.1.10',
            'as_number': 64000,
            'msgrcvd': 0
        },
        '20.1.1.10': {
            'up_down': 'never',
            'state': 'Active',
            'msgsent': 0,
            'neighbor': '20.1.1.10',
            'as_number': 65000,
            'msgrcvd': 0
        },
        'local_as_number': 64000
    }

    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_show_ip_bgp_neighbors():
    raw_result = """\
  name: 192.168.1.10, remote-as: 64000
    state: Active
    tcp_port_number: 179

    statistics:
       bgp_peer_dropped_count: 0
       bgp_peer_dynamic_cap_in_count: 0
       bgp_peer_dynamic_cap_out_count: 0
       bgp_peer_established_count: 0
       bgp_peer_keepalive_in_count: 0
       bgp_peer_keepalive_out_count: 0
       bgp_peer_notify_in_count: 0
       bgp_peer_notify_out_count: 0
       bgp_peer_open_in_count: 0
       bgp_peer_open_out_count: 0
       bgp_peer_readtime: 611931
       bgp_peer_refresh_in_count: 0
       bgp_peer_refresh_out_count: 0
       bgp_peer_resettime: 611931
       bgp_peer_update_in_count: 0
       bgp_peer_update_out_count: 0
       bgp_peer_uptime: 0

  name: 20.1.1.1, remote-as: 65000
    state: Active
    tcp_port_number: 179

    statistics:
       bgp_peer_dropped_count: 0
       bgp_peer_dynamic_cap_in_count: 0
       bgp_peer_dynamic_cap_out_count: 0
       bgp_peer_established_count: 0
       bgp_peer_keepalive_in_count: 0
       bgp_peer_keepalive_out_count: 0
       bgp_peer_notify_in_count: 0
       bgp_peer_notify_out_count: 0
       bgp_peer_open_in_count: 0
       bgp_peer_open_out_count: 0
       bgp_peer_readtime: 611931
       bgp_peer_refresh_in_count: 0
       bgp_peer_refresh_out_count: 0
       bgp_peer_resettime: 611931
       bgp_peer_update_in_count: 0
       bgp_peer_update_out_count: 0
       bgp_peer_uptime: 0

  name: 20.1.1.10, remote-as: 65000
    state: Active
    tcp_port_number: 179

    statistics:
       bgp_peer_dropped_count: 0
       bgp_peer_dynamic_cap_in_count: 0
       bgp_peer_dynamic_cap_out_count: 0
       bgp_peer_established_count: 0
       bgp_peer_keepalive_in_count: 0
       bgp_peer_keepalive_out_count: 0
       bgp_peer_notify_in_count: 0
       bgp_peer_notify_out_count: 0
       bgp_peer_open_in_count: 0
       bgp_peer_open_out_count: 0
       bgp_peer_readtime: 611931
       bgp_peer_refresh_in_count: 0
       bgp_peer_refresh_out_count: 0
       bgp_peer_resettime: 611931
       bgp_peer_update_in_count: 0
       bgp_peer_update_out_count: 0
       bgp_peer_uptime: 0
    """

    result = parse_show_ip_bgp_neighbors(raw_result)

    expected = {
        '20.1.1.1': {
            'state': 'Active',
            'bgp_peer_keepalive_out_count': 0,
            'bgp_peer_readtime': 611931,
            'bgp_peer_uptime': 0,
            'tcp_port_number': 179,
            'bgp_peer_refresh_in_count': 0,
            'bgp_peer_notify_in_count': 0,
            'bgp_peer_keepalive_in_count': 0,
            'bgp_peer_resettime': 611931,
            'name': '20.1.1.1',
            'bgp_peer_update_out_count': 0,
            'bgp_peer_open_in_count': 0,
            'bgp_peer_open_out_count': 0,
            'bgp_peer_dynamic_cap_in_count': 0,
            'remote_as': 65000,
            'bgp_peer_established_count': 0,
            'bgp_peer_notify_out_count': 0,
            'bgp_peer_refresh_out_count': 0,
            'bgp_peer_dynamic_cap_out_count': 0,
            'bgp_peer_dropped_count': 0,
            'bgp_peer_update_in_count': 0
        },
        '20.1.1.10': {
            'state': 'Active',
            'bgp_peer_keepalive_out_count': 0,
            'bgp_peer_readtime': 611931,
            'bgp_peer_uptime': 0,
            'tcp_port_number': 179,
            'bgp_peer_refresh_in_count': 0,
            'bgp_peer_notify_in_count': 0,
            'bgp_peer_keepalive_in_count': 0,
            'bgp_peer_resettime': 611931,
            'name': '20.1.1.10',
            'bgp_peer_update_out_count': 0,
            'bgp_peer_open_in_count': 0,
            'bgp_peer_open_out_count': 0,
            'bgp_peer_dynamic_cap_in_count': 0,
            'remote_as': 65000,
            'bgp_peer_established_count': 0,
            'bgp_peer_notify_out_count': 0,
            'bgp_peer_refresh_out_count': 0,
            'bgp_peer_dynamic_cap_out_count': 0,
            'bgp_peer_dropped_count': 0,
            'bgp_peer_update_in_count': 0
        },
        '192.168.1.10': {
            'state': 'Active',
            'bgp_peer_keepalive_out_count': 0,
            'bgp_peer_readtime': 611931,
            'bgp_peer_uptime': 0,
            'tcp_port_number': 179,
            'bgp_peer_refresh_in_count': 0,
            'bgp_peer_notify_in_count': 0,
            'bgp_peer_keepalive_in_count': 0,
            'bgp_peer_resettime': 611931,
            'name': '192.168.1.10',
            'bgp_peer_update_out_count': 0,
            'bgp_peer_open_in_count': 0,
            'bgp_peer_open_out_count': 0,
            'bgp_peer_dynamic_cap_in_count': 0,
            'remote_as': 64000,
            'bgp_peer_established_count': 0,
            'bgp_peer_notify_out_count': 0,
            'bgp_peer_refresh_out_count': 0,
            'bgp_peer_dynamic_cap_out_count': 0,
            'bgp_peer_dropped_count': 0,
            'bgp_peer_update_in_count': 0
        }
    }

    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_show_ip_bgp():
    raw_result = """\
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
              i internal, S Stale, R Removed
Origin codes: i - IGP, e - EGP, ? - incomplete

Local router-id 2.0.0.1
   Network          Next Hop            Metric LocPrf Weight Path
*> 10.1.0.10/32     0.0.0.0                  0      0  32768  i
*> 10.1.0.14/32     0.0.0.0                  0      0  32768  i
*> 10.2.0.10/32     20.1.1.1                 0      0      0 65000 64100 i
*  10.2.0.10/32     20.1.1.10                0      0      0 65000 64100 i
*> 10.2.0.14/32     20.1.1.1                 0      0      0 65000 64100 i
*  10.2.0.14/32     20.1.1.10                0      0      0 65000 64100 i
Total number of entries 6
    """

    result = parse_show_ip_bgp(raw_result)

    expected = [
        {
            'path': 'i',
            'metric': 0,
            'weight': 32768,
            'network': '10.1.0.10/32',
            'locprf': 0,
            'next_hop': '0.0.0.0',
            'route_status': '*>'
        },
        {
            'path': 'i',
            'metric': 0,
            'weight': 32768,
            'network': '10.1.0.14/32',
            'locprf': 0,
            'next_hop': '0.0.0.0',
            'route_status': '*>'
        },
        {
            'path': '65000 64100 i',
            'metric': 0,
            'weight': 0,
            'network': '10.2.0.10/32',
            'locprf': 0,
            'next_hop': '20.1.1.1',
            'route_status': '*>'
        },
        {
            'path': '65000 64100 i',
            'metric': 0,
            'weight': 0,
            'network': '10.2.0.10/32',
            'locprf': 0,
            'next_hop': '20.1.1.10',
            'route_status': '*'
        },
        {
            'path': '65000 64100 i',
            'metric': 0,
            'weight': 0,
            'network': '10.2.0.14/32',
            'locprf': 0,
            'next_hop': '20.1.1.1',
            'route_status': '*>'
        },
        {
            'path': '65000 64100 i',
            'metric': 0,
            'weight': 0,
            'network': '10.2.0.14/32',
            'locprf': 0,
            'next_hop': '20.1.1.10',
            'route_status': '*'
        }
    ]

    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_ping_repetitions():
    raw_result = """\
PING 10.0.0.9 (10.0.0.9): 100 data bytes
108 bytes from 10.0.0.9: icmp_seq=0 ttl=64 time=1.040 ms
--- 10.0.0.9 ping statistics ---
1 packets transmitted, 1 packets received, 0% packet loss
round-trip min/avg/max/stddev = 1.040/1.040/1.040/0.000 ms
    """

    result = parse_ping_repetitions(raw_result)

    expected = {
        'transmitted': 1,
        'received': 1,
        'errors': 0,
        'packet_loss': 0
    }

    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_ping6_repetitions():
    raw_result = """\
PING 2000::2 (2000::2): 100 data bytes
108 bytes from 2000::2: icmp_seq=0 ttl=64 time=0.411 ms
--- 2000::2 ping statistics ---
1 packets transmitted, 1 packets received, 0% packet loss
round-trip min/avg/max/stddev = 0.411/0.411/0.411/0.000 ms
    """

    result = parse_ping6_repetitions(raw_result)

    expected = {
        'transmitted': 1,
        'received': 1,
        'errors': 0,
        'packet_loss': 0
    }

    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_show_rib():
    raw_result = """
Displaying ipv4 rib entries

'*' denotes selected
'[x/y]' denotes [distance/metric]

*140.0.0.0/30,  1 unicast next-hops
    *via  10.10.0.2,  [20/0],  BGP
*140.0.0.4/30,  1 unicast next-hops
    *via  10.10.0.2,  [20/0],  BGP
*193.0.0.2/32,  2 unicast next-hops
    *via  50.0.0.2,  [1/0],  static
    *via  56.0.0.3,  [1/0],  static
*10.10.0.0/24,  1 unicast next-hops
    *via  1,  [0/0],  connected

Displaying ipv6 rib entries

'*' denotes selected
'[x/y]' denotes [distance/metric]

*2002::/64,  1 unicast next-hops
    *via  4,  [0/0],  connected
*2010:bd9::/32,  3 unicast next-hops
    *via  2005::2,  [1/0],  static
    *via  2001::2,  [1/0],  static
    via  2002::2,  [1/0],  static
    """

    result = parse_show_rib(raw_result)

    expected = {
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
                'id': '140.0.0.4',
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

    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_show_running_config():
    raw_result = """\
    Current configuration:
!
!
!
router bgp 64001
     bgp router-id 2.0.0.1
     network 10.240.0.2/32
     network 10.240.1.2/32
     network 10.240.2.2/32
     network 10.240.3.2/32
     network 10.240.4.2/32
!
"""

    result = parse_show_running_config(raw_result)

    expected = {
        'bgp':
            {'64001':
                {'networks': ['10.240.0.2/32',
                              '10.240.1.2/32',
                              '10.240.2.2/32',
                              '10.240.3.2/32',
                              '10.240.4.2/32'],
                 'router_id': '2.0.0.1'}
             }
    }

    ddiff = DeepDiff(result, expected)
    assert not ddiff


def test_parse_show_ip_route():
    raw_result = """
Displaying ipv4 routes selected for forwarding

'[x/y]' denotes [distance/metric]

140.0.0.0/30,  1 unicast next-hops
    via  10.10.0.2,  [20/0],  bgp
140.0.0.4/30,  1 unicast next-hops
    via  10.10.0.2,  [20/0],  bgp
10.10.0.0/24,  1 unicast next-hops
    via  1,  [0/0],  connected
193.0.0.2/32,  2 unicast next-hops
    via  50.0.0.2,  [1/0],  static
    via  56.0.0.3,  [1/0],  static
    """

    result = parse_show_ip_route(raw_result)

    expected = [
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
            'id': '140.0.0.4',
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

    ddiff = DeepDiff(result, expected)
    assert not ddiff
