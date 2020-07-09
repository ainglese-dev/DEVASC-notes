#!/usr/bin/env python

import requests

from config import Sandbox

creds = (Sandbox.USERNAME, Sandbox.PASSWORD)

url = f"http://{Sandbox.HOSTS[0]}:{Sandbox.REST_PORT}/ins"
myheaders = {"content-type": "application/json"}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "sid",
        "input": "show ip int b",
        "output_format": "json",
    }
}

resp = requests.post(url, json=payload, headers=myheaders, auth=creds)
