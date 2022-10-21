<p align="center">
<img src="https://github.com/martinkubecka/redSnooper/blob/main/images/banner.png" alt="Logo">
<p align="center"><b>redirect chain snooper</b><br>
</p>

---
## Table of Contents

1. Docker version
    - Pre-requisites
    - Usage
2. Local version
    - Pre-requisites
        - Software
        - VPN configuration
        - Firefox (gecko) driver
        - Virtual environment
    - Usage

---
## Docker version

### Pre-requisites

### Usage

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

If pip is not in your system
```
$ sudo apt-get install python-pip
```

Then install virtualenv
```
$ pip install virtualenv
```

Now check your installation
```
$ virtualenv --version
```

Inside the projcet directory create a virtual environment called `venv`
```
$ virtualenv --python=python3 venv
```

Activate it by using the following command
```
$ source venv/bin/activate
```

You can deactivate the virtual environment from the parent folder of `venv` directory
``` 
$ deactivate
```

### Usage

---