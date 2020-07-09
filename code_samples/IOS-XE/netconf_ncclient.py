#!/usr/bin/env python
from ncclient import manager
import xmltodict

from config import Sandbox

sandbox = {
    "host": Sandbox.HOSTS[0],
    "port": Sandbox.NETCONF_PORT,
    "username": Sandbox.USERNAME,
    "password": Sandbox.PASSWORD,
    "hostkey_verify": Sandbox.HOSTKEY_VERIFY,
    "device_params": {"name": "default"},
}

# Return configuration and operational state for interface 'GigabitEthernet2'
netconf_filter = """
<filter>
  <interfaces xmlns="{capability}">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces>
<interfaces-state xmlns="{capability}">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces-state>
</filter>
"""

test_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces-ext" />
</filter>
"""

# with manager.connect(**sandbox) as m:
with manager.connect(
    host=sandbox["host"],
    port=sandbox["port"],
    username=sandbox["username"],
    password=sandbox["password"],
    hostkey_verify=sandbox["hostkey_verify"],
    device_params=sandbox["device_params"],
) as m:
    for cap in m.server_capabilities:
        if "ietf-interfaces?" in cap.lower():
            print(cap)
            capability = cap
            # print(cap)
    try:
        print(capability)
        interface_xml = m.get(netconf_filter.format(capability=capability))
        # all_the_xml = m.get(test_filter)
    finally:
        m.close_session()

# print(all_the_xml)
print(interface_xml)
# all_the_dict = xmltodict.parse(all_the_xml)
# print(all_the_dict)
# interface_data = xmltodict.parse(interface_xml)['rpc-reply']['data']
# interface_config = interface_data['interfaces']['interface']
# interface_state = interface_data['interfaces-state']['interface']

# print(f"Name: {interface_config['name']['#text']}")
# print(f"Description: {interface_config['description']}")
# print(f"Packets In: {interface_state['statistics']['in-unicast-pkts']}")
