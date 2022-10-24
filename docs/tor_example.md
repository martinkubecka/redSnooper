```
web-collector$ python main.py -u "https://webhook.site/75d7b590-e9e9-4554-a483-99cc8fa7eb6d" -n TOR

             _ _____      |                 
   ___ ___ _| |   __|___ _|_ ___ ___ ___ ___ 
  |  _| -_| . |__   | ---[o]--- | . | -_|  _|
  |_| |___|___|_____|_|_|_|_|___|  _|___|_|  
                          |     |_|          
    
[*] Using TOR for network configuration

[*] Checking if Tor is installed on your system
[*] Tor is installed

Oct 24 12:25:25.000 [notice] Bootstrapped 0% (starting): Starting
Oct 24 12:25:26.000 [notice] Bootstrapped 5% (conn): Connecting to a relay
Oct 24 12:25:41.000 [notice] Bootstrapped 10% (conn_done): Connected to a relay
Oct 24 12:25:43.000 [notice] Bootstrapped 14% (handshake): Handshaking with a relay
Oct 24 12:25:43.000 [notice] Bootstrapped 15% (handshake_done): Handshake with a relay done
Oct 24 12:25:43.000 [notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits
Oct 24 12:25:43.000 [notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits
Oct 24 12:25:43.000 [notice] Bootstrapped 95% (circuit_create): Establishing a Tor circuit
Oct 24 12:25:46.000 [notice] Bootstrapped 100% (done): Done

[*] Fetching current IP from 'https://ip.qintec.sk?json'
[*] Your current IP address is 144.172.73.34 and country is Unknown

[*] Initializing webdriver with 'Mozilla/5.0 (Windows NT 8.1) AppleWebKit/537.27.34 (KHTML, like Gecko) Chrome/54.0.2725.19 Safari/537.27.34' user agent
[*] Webdriver using proxy 'socks5://127.0.0.1:9050'
[*] Webdriver was successfully initialized

[*] REDIRECT CHAIN
https://webhook.site/75d7b590-e9e9-4554-a483-99cc8fa7eb6d

[*] Writing redirect chain URLs to a file
[*] Writing captured data to a HAR file

[*] Webdriver destruction started
[*] Webdriver was successfully destroyed

[*] Closing network connection via Tor ...
```