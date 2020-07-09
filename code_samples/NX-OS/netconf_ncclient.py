#!/usr/bin/env python

import logging
from pprint import pprint

# import xml.dom.minidom

# from pprint import pprint

from ncclient import manager

import xmltodict

from config import Sandbox

logging.basicConfig(level=logging.INFO)


# Return configuration and operational state for interface 'GigabitEthernet2'
netconf_filter = """<filter>
  <interfaces xmlns="http://openconfig.net/yang/interfaces">
    <interface>
      <name>Ethernet1/1</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="http://openconfig.net/yang/interfaces">
    <interface>
      <name>Ethernet1/1</name>
    </interface>
  </interfaces-state>
</filter>
"""

test_filter = """<filter>
  <interfaces xmlns="http://openconfig.net/yang/interfaces">
    <interface>
      <name>Loopback69</name>
      <config>
        <type />
        <mtu />
        <name />
        <description />
        <enabled />
      </config>
    </interface>
  </interfaces>
</filter>
"""

vlan_filter = """<show xmlns="http://www.cisco.com/nxos:1.0:vlan_mgr_cli">
  <vlan>
    <brief />
  </vlan>
</filter>"""

logging.info("Attempting to connect to %s", Sandbox.HOSTS[0])
with manager.connect(
    host=Sandbox.HOSTS[0],
    port=Sandbox.NETCONF_PORT,
    timeout=120,
    username=Sandbox.USERNAME,
    password=Sandbox.PASSWORD,
    hostkey_verify=Sandbox.HOSTKEY_VERIFY,
    device_params=Sandbox.DEVICE_PARAMS,
) as m:
    logging.info("Successfully connected to %s", Sandbox.HOSTS[0])
    logging.info("Searching capabilities")
    client_only_caps, server_only_caps, mutual_caps = [], [], []
    for cap in m.client_capabilities:
        if cap not in m.server_capabilities:
            client_only_caps.append(cap)
    for cap in m.server_capabilities:
        if cap in m.client_capabilities:
            mutual_caps.append(cap)
        else:
            server_only_caps.append(cap)
        logging.info("Server only capabilities:")
        pprint(server_only_caps)
        logging.info("Client only capabilities:")
        pprint(client_only_caps)
        logging.info("Mutual capabilities:")
        pprint(mutual_caps)
        # if "netconf:base" in cap.lower():
        # logging.debug("Desired capability found! Setting namespace.")
        # if "?" in cap:
        # namespace = cap.split("?")[0]
        # else:
        # namespace = cap
    try:
        # logging.info("Attempting to gather info from namespace %s", namespace)
        # print(test_filter.format(namespace=namespace))
        config_resp = m.get_config(source="running", filter=test_filter)
        # interface_resp = m.get(("subtree", test_filter))
        # vlans_resp = m.get(("subtree", vlan_filter))
    except NameError:
        logging.exception("The requested namespace is not supported!")
        # raise ValueError("The requested namespace is not supported!")

# print(all_the_xml)
# print(interface_xml)
# print(vlans)
# xml_dom = xml.dom.minidom.parseString(str(vlans))
# pprint(xmltodict.parse(vlans_resp.xml)["rpc-reply"]["data"])
# all_the_dict = xmltodict.parse(all_the_xml)
# print(all_the_dict)
# interface_data = xmltodict.parse(interface_resp.xml)
# interface_config = interface_data["interfaces"]["interface"]
# interface_state = interface_data["interfaces-state"]["interface"]
# pprint(interface_data)
print(xmltodict.parse(config_resp.xml)["rpc-reply"]["data"])
# print(f"Name: {interface_config['name']['#text']}")
# print(f"Description: {interface_config['description']}")
# print(f"Packets In: {interface_state['statistics']['in-unicast-pkts']}")
