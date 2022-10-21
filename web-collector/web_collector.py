# selenium, puppeteer, bablosoft bas [https://thehackernews.com/2022/05/hackers-increasingly-using-browser.html]

############################### UNUSED IMPORTS ###############################
# import sys
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options as chrome_options
#from selenium import webdriver
#from PIL import Image
#import pytesseract
###############################################################################

import os
import re
import sys
import json
import yaml
import random
import shutil
import requests
from seleniumwire import webdriver
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

from tor_runner import TorClient

# TODO : change printing errors to logger
# TODO : IMPLEMENT USER AGENTS TO REQUESTS !!!!!


def get_random_user_agent(user_agent_host):

    if user_agent_host == "Desktop":
        host_os = OperatingSystem.WINDOWS.value
    elif user_agent_host == "Android":
        host_os = OperatingSystem.ANDROID.value
    elif user_agent_host == "iOS":
        host_os = OperatingSystem.IOS.value
    else:
        print(f"[!] Invalid USER AGENT")
        print(f"[*] Defaulting to Dektop-Windows ...")
        host_os = OperatingSystem.WINDOWS.value

    software_names = [SoftwareName.CHROME.value,
                      SoftwareName.FIREFOX.value,
                      SoftwareName.OPERA.value]

    user_agent_rotator = UserAgent(
        software_names=software_names, operating_systems=host_os, limit=100)

    user_agent = user_agent_rotator.get_random_user_agent()

    return user_agent


def get_vpn_servers():
    # https://nordvpn.com/servers/tools/
    # https://nordvpn.com/ovpn/
    with open("vpn_servers.json", "r") as file:
        vpn_servers = json.load(file)
    return vpn_servers


def is_ip_valid(current_ip):
    match = re.match(
        r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", current_ip)

    if bool(match) is False:
        return False

    for part in current_ip.split("."):
        if int(part) < 0 or int(part) > 255:
            return False

    return True


def is_program_installed(program_name):
    return shutil.which(program_name)


def load_config():
    with open(".config.yml", "r") as ymlfile:
        config = yaml.safe_load(ymlfile)
    return config


class ENTITY_WEB_COLLECTOR:
    def __init__(self, network_option, user_agent_host, vpn_country):
        self.network_option = network_option   # "MOBILE_DATA", "VPN", "TOR"
        self.proxies = None
        self.user_agent_host = get_random_user_agent(
            user_agent_host)    # "Desktop", "Android", "iOS"
        self.vpn_country = vpn_country
        self.default_vpn_country = "France"
        self.profile_config = load_config()
        self.tor = None
        self.socks_port = None
        self.driver = None

    def initialize_network(self):
        network_option = self.network_option

        if network_option == "MOBILE_DATA":
            print("[*] Using MOBILE DATA for network configuration")

        elif network_option == "VPN":
            print("[*] Using VPN for network configuration")

            print(f"\n[*] Checking if OpenVPN is installed on your system")
            is_vpn_installed = is_program_installed("openvpn")

            if not is_vpn_installed:
                print(f"\n[!] OpenVPN is not installed on your system\n")
                print("\nExiting program ...\n")
                exit(1)
            else:
                print(f"[*] OpenVPN is installed")

                vpn_servers = get_vpn_servers()

                if self.vpn_country is None:
                    print(f"[!] Country for VPN server was not selected")
                    print(f"[*] Defaulting to '{self.default_vpn_country}'")

                elif self.vpn_country == "Slovakia":
                    sk_vpn_list = vpn_servers['vpn_servers']['Slovakia']
                    randodm_vpn_server = random.choice(sk_vpn_list)

                elif self.vpn_country == "France":
                    fr_vpn_list = vpn_servers['vpn_servers']['France']
                    randodm_vpn_server = random.choice(fr_vpn_list)

                elif self.vpn_country == "United_States":
                    us_vpn_list = vpn_servers['vpn_servers']['United_States']
                    randodm_vpn_server = random.choice(us_vpn_list)

                print(
                    f"[*] Connecting to '{self.vpn_country}'")
                # connect_cmd = f"openvpn --daemon --config {randodm_vpn_server} &"
                connect_cmd = f"sudo openvpn --daemon --config {randodm_vpn_server} &"
                os.system(connect_cmd)

        elif network_option == "TOR":
            print("[*] Using TOR for network configuration")
            is_tor_installed = is_program_installed("tor")

            if not is_tor_installed:
                print(f"\n[!] Tor is not installed on your system\n")
                print("\nExiting program ...\n")
                exit(1)
            else:
                print(f"[*] Tor is installed\n")
                self.tor = TorClient()
                self.proxies = self.tor.proxies
                self.socks_port = self.tor.socks_port
                self.tor.start_tor()

    def stop_network(self):
        if self.network_option == "VPN":
            print(f"[*] Closing network connection via VPN ...\n")
            os.system("pkill -9 openvpn")
            # os.system("sudo pkill -9 openvpn")
        if self.network_option == "TOR":
            print(f"[*] Closing network connection via Tor ...\n")
            os.system("pkill -9 tor")
            # os.system("sudo pkill -9 tor")

    def check_ip(self):
        ip_check_urls = ["https://api.myip.com",
                         "https://ip.qintec.sk?json", "https://icanhazip.com/"]

        forbidden_ip_prefix = self.profile_config['profile']['work_ip_prefix']

        try:
            print(f"\n[*] Fetching current IP from '{ip_check_urls[1]}'")
            response = requests.get(ip_check_urls[0], proxies=self.proxies)
            status = response.status_code

            if status != requests.codes.ok:
                print(
                    f'\n[!] Error encountered with Status Code: {status} while checking the current IP\n')
                sys.exit(5)

            data = json.loads(response.content.decode("utf-8"))
            current_ip = data['ip']
            current_country = data['country']
            # current_cc = data['cc']

            check_ip = is_ip_valid(current_ip)
            if check_ip:
                print(
                    f"[*] Your current IP address is {current_ip} and country is {current_country}")
            else:
                print(
                    f"[!] IP address {current_ip} is not valid or can not be checked")
                sys.exit(1)

            if forbidden_ip_prefix in current_ip:
                print(
                    f"\n[!] NOT USING MOBILE DATA / VPN / TOR IS STRICTLY FORBIDDEN")
                print(f"\nExiting program ...\n")
                sys.exit(1)

            return current_country

        except:
            print(f"[!] Error encountered while fetching current IP")
            print(f"\nExiting program ...\n")
            sys.exit(1)

    def initialize_driver(self):
        print(f"\n[*] Initializing webdriver")

        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        firefox_options.set_preference('general.useragent.override', '')

        if self.network_option == "TOR":
            print(f"[*] Webdriver using proxy '{self.proxies['http']}'")
            seleniumwire_options = {
                'headless': True,
                'proxy': {
                    'http': 'socks5://127.0.0.1:9050',
                    'https': 'socks5://127.0.0.1:9050',
                    'no_proxy': 'localhost,127.0.0.1'
                },
                'enable_har': True
            }
        else:
            seleniumwire_options = {'enable_har': True}

        try:
            # self.driver = webdriver.Firefox(
            #     executable_path='/usr/bin/geckodriver',
            #     options=firefox_options,
            #     seleniumwire_options=seleniumwire_options
            # )
            self.driver = webdriver.Firefox(
                options=firefox_options,
                seleniumwire_options=seleniumwire_options
            )

            print(f"[*] Webdriver was successfully initialized\n")
        except Exception as e:
            print(f"[!] Webdriver initialization failed with {str(e)}\n")

    def destroy_driver(self):
        print(f"\n[*] Webdriver destruction started")
        try:
            self.driver.close()
            print(f"[*] Webdriver was successfully destroyed\n")
        except Exception as e:
            print(f"[!] Webdriver destruction failed with {str(e)}\n")

    def crawl(self, url):
        self.driver.get(url)

        print(f"[*] REDIRECT CHAIN")
        for request in self.driver.requests:
            if request.response:
                if not "mozilla" in request.url:
                    print(request.url)

        with open('response.har', 'w') as har_file:
            print(self.driver.har, file=har_file)

            # request_counter = 0

            # for request in self.driver.requests:
            #     request_counter = request_counter + 1
            #     if request.response:
            #         with open('_'.join(str(request_counter), request.url.split('/')[2], request.response.status_code), 'w') as out_file:
            #             print(request.response.body, file=out_file)
