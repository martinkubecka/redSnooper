<p align="center">
<img src="https://github.com/martinkubecka/redSnooper/blob/main/docs/banner.png" alt="Logo">
<p align="center"><b>Redirect chain analysis tool with random user agents supporting VPN and TOR as a network configuration.</b><br>
</p>

---
**Table of Contents**
- [Local version](#local-version)
  - [Pre-requisites](#pre-requisites)
  - [Software](#software)
  - [VPN configuration](#vpn-configuration)
  - [Firefox (gecko) driver](#firefox-gecko-driver)
    - [Virtual environment](#virtual-environment)
  - [Usage](#usage)
    - [Examples](#examples)
- [Docker version](#docker-version)
  - [Pre-requisites](#pre-requisites-1)
    - [Docker](#docker)
    - [Docker Compose](#docker-compose)
    - [VPN configuration](#vpn-configuration-1)
  - [Usage](#usage-1)

---
## Local version

### Pre-requisites

- clone this project with the following command

```
$ git clone <URL>
```

### Software

- user your package manager to install [Tor](https://community.torproject.org/onion-services/setup/install/) and [OpenVPN](https://community.openvpn.net/openvpn/wiki/HOWTO#InstallingOpenVPN)

### VPN configuration

1. get a [NordVPN](https://nordvpn.com/) account
2. download and unzip NordVPN configuration files for OpenVPN manual setup
3. create 'vpn_login.txt' file in 'web-collector' directory and put your NordVPN credentials (email and password) on the separate lines
4. run the two `find` commands below to add your 'vpn_login.txt' authentication file to the OpenVPN configuration files

```
$ cd <DIR/web-collector>
web-collector $ wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip -O ovpn.zip 
web-collector $ unzip ovpn.zip
web-collector $ rm ovpn.zip
web-collector $ cp vpn_login.txt ovpn_udp/
web-collector $ cp vpn_login.txt ovpn_tcp/

web-collector $ find ovpn_udp/ -type f -name "*nordvpn.com.udp.ovpn" -print0 | xargs -0 sed -i 's+auth-user-pass+auth-user-pass vpn_login.txt+'

web-collector $ find ovpn_tcp/ -type f -name "*nordvpn.com.tcp.ovpn" -print0 | xargs -0 sed -i 's+auth-user-pass+auth-user-pass vpn_login.txt+'

web-collector $ rm vpn_login.txt

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

#### Virtual environment

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

### Usage

```
usage: main.py [-h] -u URL [-n OPTION] [-c COUNTRY] [-a OPTION] [-v LEVEL]

Redirect chain analysis tool with random user agents supporting VPN and TOR as a network configuration

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL for analysis (use double quotes)
  -n OPTION, --network OPTION
                        network configuration option [MOBILE/VPN/TOR] (default: MOBILE)
  -c COUNTRY, --country COUNTRY
                        VPN country [SK/FR/US] (required if VPN is selected)
  -a OPTION, --user-agent OPTION
                        user agent [Desktop/Android/iOS] (default: Desktop)
  -v LEVEL, --verbosity LEVEL
                        redirect chain verbosity [0/1] (default: 0)

```

#### Examples

- [Mobile Data](https://github.com/martinkubecka/redSnooper/blob/main/docs/mobile_data_example.md)
- [VPN](https://github.com/martinkubecka/redSnooper/blob/main/docs/vpn_example.md)
- [TOR](https://github.com/martinkubecka/redSnooper/blob/main/docs/tor_example.md)

---
## Docker version

### Pre-requisites

- clone this project with the following command

```
$ git clone <URL>
```

#### Docker

- user your package manager to install [Docker](https://docs.docker.com/engine/install/)

#### Docker Compose

1. download the latest **Docker Compose** release and named it `docker-compose`
    - https://github.com/docker/compose
2. add execution to the binary
3. move the binary to the `/usr/local/bin/` directory
4. verify the installation by checking the version

```
$ sudo chmod +x docker-compose
$ sudo mv docker-compose /usr/local/bin/
$ docker-compose --version
```

#### VPN configuration

- get a [NordVPN](https://nordvpn.com/) account


### Usage

- run `docker-compose up -d` command inside the `readSnooper` directory where the `docker-compose.yml` file is located
- run `curl http://127.0.0.1:3000/status` to verify if the container is running

> TODO ?Flask?

---