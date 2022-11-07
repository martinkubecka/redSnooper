<p align="center">
<img src="https://github.com/martinkubecka/redSnooper/blob/main/docs/banner.png" alt="Logo">
<p align="center"><b>Redirect chain analysis tool with random user agents supporting VPN and TOR as a network configuration.</b><br>
</p>

---
**Table of Contents**
- [Pre-requisites](#pre-requisites)
  - [Software](#software)
  - [VPN configuration](#vpn-configuration)
  - [Firefox (gecko) driver](#firefox-gecko-driver)
  - [Virtual environment](#virtual-environment)
- [Usage](#usage)
  - [Redirect Chain Examples](#redirect-chain-examples)
  - [Check HTTP Status Code Examples](#check-http-status-code-examples)
- [To-Do](#to-do)


---
## Pre-requisites

- clone this project with the following command

```
$ git clone https://github.com/martinkubecka/redSnooper.git
```

### Software

- user your package manager to install [Tor](https://community.torproject.org/onion-services/setup/install/) and [OpenVPN](https://community.openvpn.net/openvpn/wiki/HOWTO#InstallingOpenVPN)

### VPN configuration

1. get a [NordVPN](https://nordvpn.com/) account
2. download and unzip NordVPN configuration files for OpenVPN manual setup in to the `config` directory 
3. create `vpn_login.txt` file in the `config` directory and put your NordVPN credentials (email and password) on the separate lines
4. copy your `vpn_login.txt` to the `ovpn_udp` and `ovpn_tcp` directories
5. run the two `find` commands below to add your `vpn_login.txt` authentication file to the OpenVPN configuration files

```
$ cd config/
config$ wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip -O ovpn.zip 
config$ unzip ovpn.zip
config$ rm ovpn.zip
config$ cp vpn_login.txt ovpn_udp/
config$ cp vpn_login.txt ovpn_tcp/
config$ find ovpn_udp/ -type f -name "*nordvpn.com.udp.ovpn" -print0 | xargs -0 sed -i 's+auth-user-pass+auth-user-pass config/ovpn_tcp/vpn_login.txt+'
config$ find ovpn_tcp/ -type f -name "*nordvpn.com.tcp.ovpn" -print0 | xargs -0 sed -i 's+auth-user-pass+auth-user-pass config/ovpn_tcp/vpn_login.txt+'
config$ rm vpn_login.txt
```

### Firefox (gecko) driver

1. download the latest release of **geckodriver** from https://github.com/mozilla/geckodriver/releases
2. extract the file
3. make the file executable
4. move the **geckodriver** to the `/usr/local/bin/` directory  

```
$ wget https://github.com/mozilla/geckodriver/releases/download/v0.*.*/geckodriver-v0.*.*-linux64.tar.gz
$ tar -xvzf geckodriver* 
$ chmod +x geckodriver
$ sudo mv geckodriver /usr/local/bin/
```

### Virtual environment

1. use your package manager to install `python-pip` if it is not present on your system
3. install `virtualenv`
4. verify installation by checking the `virtualenv` version
5. inside the project directory create a virtual environment called `venv`
6. activate it by using the `source` command
7. you can deactivate the virtual environment from the parent folder of `venv` directory with the `deactivate` command

```
$ sudo apt-get install python-pip
$ pip install virtualenv
$ virtualenv --version
$ virtualenv --python=python3 venv
$ source venv/bin/activate
$ deactivate
```

## Usage

```
usage: redSnooper.py [-h] -u URL [-n OPTION] [-c COUNTRY] [-a OPTION] [-v LEVEL] [--check]

Redirect chain analysis tool with random user agents supporting VPN and TOR as a network configuration

options:
  -h, --help                      show this help message and exit
  -u URL, --url URL               URL for analysis (use double quotes)
  -n OPTION, --network OPTION     network configuration option [VPN/TOR] (default: current network configuration)
  -c COUNTRY, --country COUNTRY   VPN country [SK/FR/US] (required if VPN is selected)
  -a OPTION, --user-agent OPTION  user agent [Desktop/Android/iOS] (default: Desktop)
  -v LEVEL, --verbosity LEVEL     redirect chain verbosity [0/1] (default: 0)
  --check                         check HTTP status code
```

### Redirect Chain Examples

- [Current network configuration](https://github.com/martinkubecka/redSnooper/blob/main/docs/redirect_chain/no_configuration_example.md)
- [VPN](https://github.com/martinkubecka/redSnooper/blob/main/docs/redirect_chain/vpn_example.md)
- [TOR](https://github.com/martinkubecka/redSnooper/blob/main/docs/redirect_chain/tor_example.md)

### Check HTTP Status Code Examples

- [Current network configuration](https://github.com/martinkubecka/redSnooper/blob/main/docs/check/no_configuration_example.md)
- [VPN](https://github.com/martinkubecka/redSnooper/blob/main/docs/check/vpn_example.md)
- [TOR](https://github.com/martinkubecka/redSnooper/blob/main/docs/check/tor_example.md)

---
## To-Do

- [ ] load multiple URLs from file for HTTP status code check
- [ ] add additional verbosity level to hide js/css/etc. files
- [ ] implement logging
- [ ] support CIDR notation for checking forbidden IP addresses
- [ ] change loading VPN configurations from a json file to dynamically loading paths
- [ ] support more countries with VPN servers 
- [ ] implement proper whitelist domain filtering