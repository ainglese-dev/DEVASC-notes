#!/usr/bin/env python

sandbox = {
    "host": "172.16.30.101",
    "netconf_port": "830",
    "rest_port": "443",
    "username": "cisco",
    "password": "cisco",
    "hostkey_verify": False,
    "device_params": {"name": "nexus"},
}


class Sandbox(object):
    HOSTS = ["172.16.30.101", "172.16.30.102", "172.16.30.103", "172.16.30.104"]
    NETCONF_PORT = "830"
    REST_PORT = "443"
    USERNAME = "cisco"
    PASSWORD = "cisco"
    HOSTKEY_VERIFY = False
    DEVICE_PARAMS = {"name": "nexus"}
