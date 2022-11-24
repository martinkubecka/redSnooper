import os
import re
import sys
import json
import yaml
import random
import shutil
import logging
import requests
import time
import tldextract
from colorama import Fore
from seleniumwire import webdriver
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

from webcollector.tor_client import TorClient


def get_random_user_agent(user_agent_host):

    if user_agent_host == "Desktop":
        host_os = OperatingSystem.WINDOWS.value
    elif user_agent_host == "Android":
        host_os = OperatingSystem.ANDROID.value
    elif user_agent_host == "iOS":
        host_os = OperatingSystem.IOS.value
    else:
        print(
            f"{Fore.YELLOW}[{time.strftime('%H:%M:%S')}] [WARNING] Invalid User-Agent{Fore.RESET}")
        logging.warning("Invalid User-Agent")
        print(
            f"[{time.strftime('%H:%M:%S')}] [INFO] Defaulting to 'Dektop-Windows' User-Agent ...")
        logging.info("Defaulting to 'Dektop-Windows' User-Agent")

        host_os = OperatingSystem.WINDOWS.value

    software_names = [SoftwareName.CHROME.value,
                      SoftwareName.FIREFOX.value,
                      SoftwareName.OPERA.value]

    user_agent_rotator = UserAgent(
        software_names=software_names, operating_systems=host_os, limit=100)

    user_agent = user_agent_rotator.get_random_user_agent()

    return user_agent


def get_vpn_servers():
    ##################### TESTING random vpn config #####################
    # import random
    # import os
    # import sys

    # ovpn_tcp_configs = f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/config/ovpn_tcp/"
    # ovpn_udp_configs = f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/config/ovpn_udp/"
    # random_vpn_config = random.choice(os.listdir(ovpn_tcp_configs))
    # vpn_config_path = f"{ovpn_tcp_configs}{random_vpn_config}"
    # print(vpn_config_path)

    # https://nordvpn.com/servers/tools/
    # https://nordvpn.com/ovpn/

    vpn_servers_config_path = f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/config/vpn_servers.json"
    with open(vpn_servers_config_path, "r") as file:
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
    with open(f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/config/config.yml", "r") as ymlfile:
        config = yaml.safe_load(ymlfile)
    return config


def get_domain_whitelist():
    with open(f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/helpers/domains.txt", "r") as file:
        domains = file.read().splitlines()
    return domains


class WebCollector:
    def __init__(self, network_option, user_agent_host, vpn_country, verbosity):
        self.network_option = network_option   # "MOBILE_DATA", "VPN", "TOR"
        self.proxies = None
        self.user_agent = get_random_user_agent(
            user_agent_host)    # "Desktop", "Android", "iOS"
        self.vpn_country = vpn_country
        self.default_vpn_country = "France"
        self.profile_config = load_config()
        self.tor = None
        self.socks_port = None
        self.driver = None
        self.verbosity = verbosity
        self.domain_whitelist = get_domain_whitelist()

    def initialize_network(self):
        network_option = self.network_option

        if network_option == "MOBILE_DATA":
            print(
                f"[{time.strftime('%H:%M:%S')}] [INFO] Using current network configuration")
            logging.info("Using current network configuration")

        elif network_option == "VPN":
            print(
                f"[{time.strftime('%H:%M:%S')}] [INFO] Using VPN for network configuration")
            logging.info("Using VPN for network configuration")

            print(
                f"[{time.strftime('%H:%M:%S')}] [INFO] Checking if OpenVPN is installed on your system ...")
            logging.info("Checking if OpenVPN is installed on your system")
            is_vpn_installed = is_program_installed("openvpn")

            if not is_vpn_installed:
                print(
                    f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] OpenVPN is not installed on your system{Fore.RESET}")
                logging.error("OpenVPN is not installed on your system")
                print("\nExiting program ...\n")
                exit(1)
            else:
                print(
                    f"{Fore.GREEN}[{time.strftime('%H:%M:%S')}] [INFO] OpenVPN is installed{Fore.RESET}")
                logging.info("OpenVPN is installed")
                vpn_servers = get_vpn_servers()

                if self.vpn_country == "Slovakia":
                    sk_vpn_list = vpn_servers['vpn_servers']['Slovakia']
                    random_vpn_server = random.choice(sk_vpn_list)

                elif self.vpn_country == "France":
                    fr_vpn_list = vpn_servers['vpn_servers']['France']
                    random_vpn_server = random.choice(fr_vpn_list)

                elif self.vpn_country == "United States":
                    us_vpn_list = vpn_servers['vpn_servers']['United States']
                    random_vpn_server = random.choice(us_vpn_list)

                try:
                    print(
                        f"[{time.strftime('%H:%M:%S')}] [INFO] Connecting to '{self.vpn_country}' ...")
                    logging.info(f"Connecting to '{self.vpn_country}")
                    connect_cmd = f"sudo openvpn --daemon --config {random_vpn_server} &"
                except:
                    print(
                        f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] Error encountered while running '{connect_cmd}'{Fore.RESET}")
                    logging.error(
                        f"Error encountered while running '{connect_cmd}'")
                    self.stop_network()
                    print(f"\nExiting program ...\n")
                    exit(1)
                os.system(connect_cmd)

        elif network_option == "TOR":
            print(
                f"[{time.strftime('%H:%M:%S')}] [INFO] Using TOR for network configuration ...")
            logging.info("Using TOR for network configuration")

            print(
                f"[{time.strftime('%H:%M:%S')}] [INFO] Checking if Tor is installed on your system ...")
            logging.info("Checking if Tor is installed on your system")
            is_tor_installed = is_program_installed("tor")

            if not is_tor_installed:
                print(
                    f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] Tor is not installed on your system{Fore.RESET}")
                logging.error("Tor is not installed on your system")
                print("\nExiting program ...\n")
                exit(1)
            else:
                print(
                    f"{Fore.GREEN}[{time.strftime('%H:%M:%S')}] [INFO] Tor is installed{Fore.RESET}")
                logging.info("Tor is installed")
                self.tor = TorClient()
                self.proxies = self.tor.proxies
                self.socks_port = self.tor.socks_port
                try:
                    print(
                        f"[{time.strftime('%H:%M:%S')}] [INFO] Initiating Tor bootstrapping ...\n")
                    logging.info("Initiating Tor bootstrapping")
                    self.tor.start_tor()
                    print("\n")
                except:
                    print(
                        f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] Error encountered while establishing a Tor circuit{Fore.RESET}")
                    logging.error(
                        "Error encountered while establishing a Tor circuit")
                    self.stop_network()
                    print(f"\nExiting program ...\n")
                    exit(1)

    def stop_network(self):
        if self.network_option == "VPN":
            print(
                f"[{time.strftime('%H:%M:%S')}] [INFO] Closing network connection via VPN ...")
            logging.info("Closing network connection via VPN")
            os.system("sudo pkill -9 openvpn")
        if self.network_option == "TOR":
            print(
                f"[{time.strftime('%H:%M:%S')}] [INFO] Closing network connection via Tor ...")
            logging.info("Closing network connection via Tor")
            os.system("sudo pkill -9 tor")

    def check_ip(self):
        ip_check_urls = ["https://api.myip.com",
                         "https://ip.qintec.sk?json", "https://icanhazip.com/"]

        forbidden_ip_prefix = self.profile_config['profile']['work_ip_prefix']

        try:
            print(
                f"[{time.strftime('%H:%M:%S')}] [INFO] Fetching current IP from '{ip_check_urls[1]}' ...")
            logging.info(f" Fetching current IP from '{ip_check_urls[1]}'")
            response = requests.get(ip_check_urls[0], proxies=self.proxies)
            status = response.status_code

            if status != requests.codes.ok:
                print(
                    f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] Error encountered with Status Code: {status} while checking the current IP{Fore.RESET}")
                logging.error(
                    "Error encountered with Status Code: {status} while checking the current IP")
                sys.exit(5)

            data = json.loads(response.content.decode("utf-8"))
            current_ip = data['ip']
            current_country = data['country']
            # current_cc = data['cc']

            check_ip = is_ip_valid(current_ip)
            if check_ip:
                print(
                    f"[{time.strftime('%H:%M:%S')}] [INFO] Your current IP address is {current_ip} and country is {current_country}")
                logging.info(
                    f"Your current IP address is {current_ip} and country is {current_country}")
            else:
                print(
                    f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] IP address {current_ip} is not valid or can not be checked{Fore.RESET}")
                logging.error(
                    f"IP address {current_ip} is not valid or can not be checked")

            if forbidden_ip_prefix in current_ip:
                print(
                    f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] NOT USING MOBILE DATA / VPN / TOR IS STRICTLY FORBIDDEN{Fore.RESET}")
                logging.error(
                    f"NOT USING MOBILE DATA / VPN / TOR IS STRICTLY FORBIDDEN")
                print(f"\nExiting program ...\n")
                sys.exit(1)

            return current_country

        except Exception as e:
            print(
                f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] Error encountered while fetching current IP{Fore.RESET}")
            logging.error(f"Error encountered while fetching current IP")
            self.stop_network()
            print(f"\nExiting program ...\n")
            sys.exit(1)

    def initialize_driver(self):
        print(f"[{time.strftime('%H:%M:%S')}] [INFO] Initializing webdriver with '{self.user_agent}' User-Agent")
        logging.info(
            f"Initializing webdriver with '{self.user_agent}' User-Agent")

        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        firefox_options.set_preference(
            'general.useragent.override', self.user_agent)

        if self.network_option == "TOR":
            print(
                f"[{time.strftime('%H:%M:%S')}] [INFO] Webdriver using proxy '{self.proxies['http']}'")
            logging.info(f"Webdriver using proxy '{self.proxies['http']}'")

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
            self.driver = webdriver.Firefox(
                options=firefox_options,
                seleniumwire_options=seleniumwire_options,
                service_log_path="logs/geckodriver.log"
            )
            print(
                f"{Fore.GREEN}[{time.strftime('%H:%M:%S')}] [INFO] Webdriver was successfully initialized{Fore.RESET}")
            logging.info(f"Webdriver was successfully initialized")

        except Exception as e:
            print(
                f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] Webdriver initialization failed with {str(e)}{Fore.RESET}")
            logging.error(f"Webdriver initialization failed with {str(e)}")

    def destroy_driver(self):
        print(
            f"[{time.strftime('%H:%M:%S')}] [INFO] Initiating webdriver destruction ...")
        logging.info(f"Initiating webdriver destruction")
        try:
            self.driver.close()
            print(
                f"{Fore.GREEN}[{time.strftime('%H:%M:%S')}] [INFO] Webdriver was successfully destroyed{Fore.RESET}")
            logging.info(f"Webdriver was successfully destroyed")
        except Exception as e:
            print(
                f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] Webdriver destruction failed with {str(e)}{Fore.RESET}")
            logging.error(f"Webdriver destruction failed with {str(e)}")

    def crawl(self, url):
        # TODO : add try/except for -->
        # selenium.common.exceptions.WebDriverException: Message: Reached error page: about:neterror?e=netTimeout&u=...
        self.driver.get(url)

        print(
            f"\n{Fore.YELLOW}________________ [ REDIRECT CHAIN ] ________________{Fore.RESET}")
        print()

        redirect_chain = []
        for request in self.driver.requests:
            if request.response:
                if self.verbosity == "0":   # filter out valid domains
                    excluded_file_types = [".png", ".jpg", ".bmp", ".svg", ".ico",
                                           ".gif", ".woff2", ".js", ".css"]  # TODO: add more filetypes
                    _, domain, _ = tldextract.extract(request.url)
                    if not any(domain in entry for entry in self.domain_whitelist):
                        if not any(filetype in request.url for filetype in excluded_file_types):
                            print(request.url)
                            redirect_chain.append(request.url)
                else:  # print all the entries from the redirect chain
                    print(request.url)
                    redirect_chain.append(request.url)
        print(
            f"{Fore.YELLOW}____________________________________________________{Fore.RESET}")

        redirect_chain_output_path = f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/reports/redirect_chain.txt"
        print(
            f"\n[{time.strftime('%H:%M:%S')}] [INFO] Writing redirect chain URLs to '{redirect_chain_output_path}' ...")
        logging.info(f"Writing redirect chain URLs to a file")
        with open(redirect_chain_output_path, 'w') as chain_file:
            for entry in redirect_chain:
                chain_file.write(f"{entry}\n")

        har_output_file = f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/reports/response.har"
        print(
            f"[{time.strftime('%H:%M:%S')}] [INFO] Writing captured data to '{har_output_file}'...")
        logging.info(f"Writing captured data to a HAR file")
        with open(har_output_file, 'w') as har_file:
            print(self.driver.har, file=har_file)

    def check(self, url):
        try:
            print(
                f"[{time.strftime('%H:%M:%S')}] [INFO] Checking status for '{url}'")
            logging.info(f"Checking status for '{url}'")
            response = requests.get(url, proxies=self.proxies)
            status = response.status_code
            print(
                f"[{time.strftime('%H:%M:%S')}] [INFO] Returned status code: {status}")
            logging.info(f"Returned status code: {status}")
        except Exception as e:
            if "NewConnectionError" in str(e):
                print(
                    f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] Name or service not known{Fore.RESET}")
                logging.error(f"Name or service not known", exc_info=True)
            else:
                print(
                    f"{Fore.RED}[{time.strftime('%H:%M:%S')}] [ERROR] Error encountered while checking status code{Fore.RESET}")
                logging.error(
                    f"Error encountered while checking status code", exc_info=True)
