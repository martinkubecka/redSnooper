import stem.process
import re


def get_proxies():
    # session = requests.session()
    # Tor uses the 9050 port as the default socks port
    # session.proxies
    proxies = {
        'http':  'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050',
    }
    # return session
    return proxies


class TorClient:

    def __init__(self):
        self.socks_port = 9050
        self.path = "/usr/bin/tor"
        self.proxies = get_proxies()

    def start_tor(self):
        self.process = stem.process.launch_tor_with_config(
            config={
                'SocksPort': str(self.socks_port),
            },
            init_msg_handler=lambda line: print(line) if re.search(
                'Bootstrapped', line) else False,
            tor_cmd=self.path
        )
