```
$ python redSnooper.py -u "https://t.co/de8ZIy8Vbs" -n TOR

             _ _____      |                 
   ___ ___ _| |   __|___ _|_ ___ ___ ___ ___ 
  |  _| -_| . |__   | ---[o]--- | . | -_|  _|
  |_| |___|___|_____|_|_|_|_|___|  _|___|_|  
                          |     |_|          
    
[*] Using TOR for network configuration

[*] Checking if Tor is installed on your system
[*] Tor is installed

[*] Initiating Tor bootstrapping
Nov 07 19:47:49.000 [notice] Bootstrapped 0% (starting): Starting
Nov 07 19:47:50.000 [notice] Bootstrapped 5% (conn): Connecting to a relay
Nov 07 19:47:50.000 [notice] Bootstrapped 10% (conn_done): Connected to a relay
Nov 07 19:47:51.000 [notice] Bootstrapped 14% (handshake): Handshaking with a relay
Nov 07 19:47:51.000 [notice] Bootstrapped 15% (handshake_done): Handshake with a relay done
Nov 07 19:47:51.000 [notice] Bootstrapped 20% (onehop_create): Establishing an encrypted directory connection
Nov 07 19:47:51.000 [notice] Bootstrapped 25% (requesting_status): Asking for networkstatus consensus
Nov 07 19:47:51.000 [notice] Bootstrapped 30% (loading_status): Loading networkstatus consensus
Nov 07 19:47:52.000 [notice] Bootstrapped 45% (requesting_descriptors): Asking for relay descriptors
Nov 07 19:47:53.000 [notice] Bootstrapped 52% (loading_descriptors): Loading relay descriptors
Nov 07 19:47:55.000 [notice] Bootstrapped 58% (loading_descriptors): Loading relay descriptors
Nov 07 19:47:56.000 [notice] Bootstrapped 67% (loading_descriptors): Loading relay descriptors
Nov 07 19:47:56.000 [notice] Bootstrapped 73% (loading_descriptors): Loading relay descriptors
Nov 07 19:47:56.000 [notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits
Nov 07 19:47:56.000 [notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits
Nov 07 19:47:56.000 [notice] Bootstrapped 95% (circuit_create): Establishing a Tor circuit
Nov 07 19:47:57.000 [notice] Bootstrapped 100% (done): Done

[*] Fetching current IP from 'https://ip.qintec.sk?json'
[*] Your current IP address is 185.220.101.10 and country is Unknown

[*] Initializing webdriver with 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36,gzip(gfe)' user agent
[*] Webdriver using proxy 'socks5://127.0.0.1:9050'
[*] Webdriver was successfully initialized

[*] REDIRECT CHAIN
http://trunc.us/TKoy7N
http://trunc.us/LwgIzL
http://trunc.us/kHIn2v
https://vubsluzbamaintenance.net/
https://vubsluzbamaintenance.net/login.php?success_redirect_url=%2F
https://vubsluzbamaintenance.net/login_up.php?success_redirect_url=%2F
https://vubsluzbamaintenance.net/ui-library/plesk-ui-library.css?1666242647
https://vubsluzbamaintenance.net/cp/theme/css/main.css?1666242647
https://vubsluzbamaintenance.net/cp/javascript/externals/prototype.js?1666242647
https://vubsluzbamaintenance.net/ui-library/plesk-ui-library.min.js?1666242647
https://vubsluzbamaintenance.net/cp/javascript/vendors.js?1666242647
https://vubsluzbamaintenance.net/cp/javascript/main.js?1666242647
https://vubsluzbamaintenance.net/cp/javascript/externals/require.js?1666242647
https://vubsluzbamaintenance.net/modules/notifier/global.js?1667256435
https://vubsluzbamaintenance.net/modules/letsencrypt/global.js?1667256558
https://vubsluzbamaintenance.net/images/apple-touch-icon.png?1666242647
https://vubsluzbamaintenance.net/images/favicon.svg?1666242647
https://vubsluzbamaintenance.net/cp/theme/images/logos/plesk/logo.svg?1666242647
https://vubsluzbamaintenance.net/ui-library/images/symbols.svg?6bd5879cb9a032639fb375ff6f1dcd26
https://vubsluzbamaintenance.net/ui-library/fonts/open-sans-600.woff2?098c0a7547a49b0ce57658f41c897ecd
https://vubsluzbamaintenance.net/ui-library/fonts/open-sans-regular.woff2?e7777b3c2bb7ae4d50f3abe9ee4f1eb5

[*] Writing redirect chain URLs to a file
[*] Writing captured data to a HAR file

[*] Webdriver destruction started
[*] Webdriver was successfully destroyed

[*] Closing network connection via Tor ...
```