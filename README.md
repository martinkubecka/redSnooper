<p align="center">
<img src="https://github.com/martinkubecka/redSnooper/blob/main/docs/banner.png" alt="Logo">
<p align="center"><b>redirect chain snooper</b><br>
</p>

---
## Table of Contents


1. Local version
    - Pre-requisites
        - Software
        - VPN configuration
        - Firefox (gecko) driver
        - Virtual environment
    - Usage

2. Docker version
    - Pre-requisites
        - Docker compose
    - Usage


---
## Local version

### Pre-requisites

```
$ git clone <URL>
```

### Software

- tor, openvpn

### VPN configuration

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

```
TODO
```

#### Virtual environment

1. If pip is not in your system
2. Then install virtualenv
3. Now check your installation
4. Inside the projcet directory create a virtual environment called `venv`
5. Activate it by using the following command
6. You can deactivate the virtual environment from the parent folder of `venv` directory

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
usage: main.py [-h] [-n OPTION] [-c COUNTRY] [-u OPTION] [-v LEVEL]

redSnooper

options:
  -h, --help            show this help message and exit
  -n OPTION, --network OPTION
                        network configuration option [MOBILE/VPN/TOR] (default: MOBILE)
  -c COUNTRY, --country COUNTRY
                        VPN country [SK/FR/US] (required if VPN is selected)
  -u OPTION, --user-agent OPTION
                        user agent [Desktop/Android/iOS] (default: Desktop)
  -v LEVEL, --verbosity LEVEL
                        redirect chain verbosity [0/1] (default: 0)
```

- [Mobile Data example](https://github.com/martinkubecka/redSnooper/blob/main/docs/mobile_data_example.md)
- [VPN example](https://github.com/martinkubecka/redSnooper/blob/main/docs/vpn_example.md)
- [TOR example](https://github.com/martinkubecka/redSnooper/blob/main/docs/tor_example.md)

---
## Docker version

### Pre-requisites

### Docker

- download docker

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

### Usage

- run `docker-compose up -d` command inside the `readSnooper` directory where the `docker-compose.yml` file is located
- run `curl http://127.0.0.1:3000/status` to check verify if the setup was successful

---