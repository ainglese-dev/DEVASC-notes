#!/usr/bin/env python
import requests

from config import sandbox

model = "urn:ietf:params:xml:ns:yang:ietf-interfaces"
interface = "Vlan100"
int_filter = f"interface={interface}"

url = f"https://{sandbox['host']}:{sandbox['port']}/restconf/data/{model}/{int_filter}"
creds = (sandbox["username"], sandbox["password"])
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

resp = requests.get(url, headers=headers, auth=creds, verify=False).json()
print(resp)

the_goods = resp["interfaces"]["interface"]
print(f"Name: {interface}")
print(f"Description: {the_goods['description']}")
print(f"Admin status: {the_goods['admin-status']}")
print(f"Operational status: {the_goods['oper-status']}")
