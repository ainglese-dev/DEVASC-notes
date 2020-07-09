#!/usr/bin/env python

import requests

from config import Sandbox

creds = (Sandbox.USERNAME, Sandbox.PASSWORD)
base_url = "https://{Sandbox.HOSTS[0]}:{Sandbox.PORT}/api"
headers = {"Accept: application/json"}

creds = {
    "aaaUser": {"attributes": {"name": Sandbox.USERNAME, "pwd": Sandbox.PASSWORD}}
}

login_url = f"{base_url}/aaaLogin"
token = requests.post(login_url, json=creds, headers=headers)["imdata"][0]["aaaLogi"][
    "attributes"
]["token"]
headers["X-API-Token":token]

show_version_url = f"{base_url}/node/mo/sys/showversion.json?query-target=self"
resp = requests.post(show_version_url, headers=headers)
