#!/usr/bin/env python
import urllib3
import xml.dom.minidom

import requests
import xmltodict

from config import CUCM

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = f"https://{CUCMHOST.HOST}/cucm-uds"


def convert_to_dict(nasty_xml):
    xmldata = xmltodict.parse(nasty_xml)
    return xmldata


def api_get(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    headers = {"Accept": "application/xml", "Content-Type": "application/xml"}
    creds = (CUCMHOST.USERNAME, CUCMHOST.PASSWORD)
    resp = requests.get(url, auth=creds, verify=False)


def list_users():
    endpoint = "users"
    resp = api_get(endpoint)
    xmldata = convert_to_dict(resp)
    users = xmldata["users"]["user"]
    for user in users:
        print(f"{user['lastName']} {user['firstName']}")
        print(f"ID: {user['id']}")
        print(" ")


def main():
    list_users()


if __name__ == "__main__":
    main()
