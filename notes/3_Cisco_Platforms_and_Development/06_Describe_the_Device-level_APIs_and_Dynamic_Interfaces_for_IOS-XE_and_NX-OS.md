# Describe the Device-level APIs and Dynamic Interfaces

## IOS-XE

### NETCONF

Requires 16.6

#### Enable

```
config terminal
hostname name
ip domain mydomain.biz
username cisco privilege 15 password cisco
crypto key generate rsa modulus 4096
ip ssh version 2
line vty 0 4
  login local
  transport ssh
  exit
interface loopback0
  ip address 172.16.1.32 255.255.255.0
  no shutdown
  exit
netconf ssh
netconf-yang
```

### RESTCONF

#### Enable

```
configure terminal
hostname name
ip domain mydomain.biz
username cisco privilege 15 password cisco
interface loopback0
  ip address 172.16.1.32 255.255.255.0
  no shutdown
  exit
restconf
! ip http server
ip http secure-server
ip http authentication local
```

## NX-OS

### NX-API CLI

#### Enable

`feature nxapi`

#### API Visualizer: Insieme

https://host

#### Python Example

```
import requests

creds=('admin', 'Admin_1234!')

url='http://10.10.20.95/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip int b",
    "output_format": "json"
  }
}

resp = requests.post(url,json=payload,headers=myheaders,auth=(switchuser,switchpassword))
```

### NX-API REST

#### Enable

`feature nxapi`

#### API Visualizer: Visore

https://host/visore.html

#### Python Example

```
import requests

creds=('admin', 'Admin_1234!')
base_url='https://10.10.20.95/api'
headers={'Accept: application/json'}

creds = {
    'aaaUser': {
        'attributes': {
            'name': 'admin',
            'pwd': 'Admin_1234!'
        }
    }
}

login_url=f'{base_url}/aaaLogin'
token = requests.post(url, json=creds, headers=headers)[imdata][0][aaaLogi][attributes][token]
headers['X-API-Token': token]

show_version_url=f'{base_url}/node/mo/sys/showversion.json?query-target=self'
resp = requests.post(show_version_url, headers=headers)
```

### NETCONF

#### Enable

```
configure terminal
feature netconf
```

### RESTCONF

#### Enable

```
configure terminal
feature nxapi
nxapi https port 443
feature restconf
```

### ACI

CI

#### REST API

Uses Visore like NX-API
Includes an API inspector to trace calls between GUI and API

#### Cobra SDK
Two components:
- aci-cobra
- aci-model

#### ACI Toolkit

acitoolkit.readthedocs.io
github.com/datacenter/acitoolkit

Includes SDK and example scripts


