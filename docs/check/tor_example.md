```
$ python redSnooper.py -u "https://t.co/de8ZIy8Vbs" --check -n TOR

             _ _____      |                 
   ___ ___ _| |   __|___ _|_ ___ ___ ___ ___ 
  |  _| -_| . |__   | ---[o]--- | . | -_|  _|
  |_| |___|___|_____|_|_|_|_|___|  _|___|_|  
                          |     |_|          
    
[*] Using TOR for network configuration

[*] Checking if Tor is installed on your system
[*] Tor is installed

[*] Initiating Tor bootstrapping
Nov 07 20:17:29.000 [notice] Bootstrapped 0% (starting): Starting
Nov 07 20:17:30.000 [notice] Bootstrapped 5% (conn): Connecting to a relay
Nov 07 20:17:30.000 [notice] Bootstrapped 10% (conn_done): Connected to a relay
Nov 07 20:17:30.000 [notice] Bootstrapped 14% (handshake): Handshaking with a relay
Nov 07 20:17:30.000 [notice] Bootstrapped 15% (handshake_done): Handshake with a relay done
Nov 07 20:17:30.000 [notice] Bootstrapped 45% (requesting_descriptors): Asking for relay descriptors
Nov 07 20:17:31.000 [notice] Bootstrapped 58% (loading_descriptors): Loading relay descriptors
Nov 07 20:17:32.000 [notice] Bootstrapped 63% (loading_descriptors): Loading relay descriptors
Nov 07 20:17:33.000 [notice] Bootstrapped 69% (loading_descriptors): Loading relay descriptors
Nov 07 20:17:34.000 [notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits
Nov 07 20:17:34.000 [notice] Bootstrapped 80% (ap_conn): Connecting to a relay to build circuits
Nov 07 20:17:34.000 [notice] Bootstrapped 85% (ap_conn_done): Connected to a relay to build circuits
Nov 07 20:17:34.000 [notice] Bootstrapped 89% (ap_handshake): Finishing handshake with a relay to build circuits
Nov 07 20:17:34.000 [notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits
Nov 07 20:17:34.000 [notice] Bootstrapped 95% (circuit_create): Establishing a Tor circuit
Nov 07 20:17:35.000 [notice] Bootstrapped 100% (done): Done

[*] Fetching current IP from 'https://ip.qintec.sk?json'
[*] Your current IP address is 185.220.101.10 and country is Unknown

[*] Checking HTTP status code for 'https://t.co/de8ZIy8Vbs'
[*] The following HTTP status code was returned: 200

[*] Closing network connection via Tor ...
```