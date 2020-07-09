#!/usr/bin/env python

import logging

from ydk.models.openconfig import openconfig_interfaces as oci
from ydk.providers import NetconfServiceProvider
from ydk.services import CRUDService, NetconfService

from config import Sandbox

logging.basicConfig(level=logging.INFO)


def main():
    # nc = NetconfService()
    crud = CRUDService()
    nc_provider = NetconfServiceProvider(
        address=Sandbox.HOSTS[0],
        port=Sandbox.NETCONF_PORT,
        username=Sandbox.USERNAME,
        password=Sandbox.PASSWORD,
    )

    interface = oci.Interfaces()

    test_if = oci.Interfaces.Interface()
    test_if.name = "Loopback69"

    # nc.get(nc_provider, test_if)
    crud.read(nc_provider, test_if)


if __name__ == "__main__":
    main()
