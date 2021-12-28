#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from RouterInfo import RouterInfo
import sys

VAR_CONF = {
    'router_ip': 'stridsberg.asuscomm.com',
    'router_port': 8443,
    'router_user': 'admin',
    'router_pw': '5546gurka1'
}

def main():
    router = RouterInfo(VAR_CONF['router_ip'], VAR_CONF['router_port'], VAR_CONF['router_user'], VAR_CONF['router_pw'])
    print(f"Uptime: {router.get_uptime()}")


if __name__ == "__main__":
    main()
    sys.exit(0)