# This is a python application that uses the Fortinet API to find and enumerate diferent things
# The primary use case is to find policys that would be triggered by a given IP address

import requests
import json
import argparse
import getpass
import settings

requests.packages.urllib3.disable_warnings()

Api_url = f"https://{settings.firewall_ip}/api/v2/cmdb/"
Api_headers = {
    "Authorization": f"Bearer {settings.api_token}",
    "Content-Type": "application/json"
}

Params = {
        "vdom": settings.vdom
}


def get_policys():
    return requests.get(f"{api_url}firewall/policy", headers=Api_headers, params=Params, verify=False, proxies=dict(https='socks5://127.0.0.1:11337'))


if __name__ == "__main__":
    policys = get_policys()
    print(policys.status_code)
    for policy in policys.json()["results"]:
        print(policy["policyid"])
        print(policy["srcaddr"])

