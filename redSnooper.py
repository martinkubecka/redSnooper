import platform
import argparse
from colorama import Fore

from web_collector.initialize import initialize_collector
from web_collector.initialize import initialize_driver
from web_collector.initialize import initialize_network
from web_collector.initialize import start_checking
from web_collector.initialize import start_crawling
from web_collector.initialize import destroy_drive
from web_collector.initialize import stop_network

# examples
# https://t.co/de8ZIy8Vbs
# https://tinyurl.com/2yuwn9n7


def banner():
    print(f"""
{Fore.RED}             _ {Fore.RESET}_____      |                 
{Fore.RED}   ___ ___ _| |{Fore.RESET}   __|___ _|_ ___ ___ ___ ___ 
{Fore.RED}  |  _| -_| . |{Fore.RESET}__   | ---[o]--- | . | -_|  _|
{Fore.RED}  |_| |___|___|{Fore.RESET}_____|_|_|_|_|___|  _|___|_|  
                          |     |_|          
    """)


def arg_formatter():
    """
    source : https://stackoverflow.com/questions/52605094/python-argparse-increase-space-between-parameter-and-description
    """

    def formatter(prog): return argparse.HelpFormatter(
        prog, max_help_position=52)

    return formatter


def parse_args():
    parser = argparse.ArgumentParser(formatter_class=arg_formatter(),
                                     description='Redirect chain analysis tool with random user agents supporting VPN and TOR as a network configuration')

    parser.add_argument('-u', '--url', metavar="URL", required=True,
                        help='URL for analysis (use double quotes)')
    parser.add_argument('-n', '--network', metavar="OPTION", default="NONE",
                        help='network configuration option [VPN/TOR] (default: current network configuration)')
    parser.add_argument('-c', '--country', metavar="COUNTRY", default="France",
                        help='VPN country [SK/FR/US] (required if VPN is selected)')
    parser.add_argument('-a', '--user-agent', metavar="OPTION", default="Desktop",
                        help='user agent [Desktop/Android/iOS] (default: Desktop)')
    parser.add_argument('-v', '--verbosity', metavar="LEVEL", default="0",
                        help='redirect chain verbosity [0/1] (default: 0)')
    parser.add_argument('--check', action='store_true',
                        help='check HTTP status code')

    args = parser.parse_args()
    return args


def main():
    print("\033[H\033[J", end="")
    banner()

    machine_platfrom = platform.system().lower()
    if not machine_platfrom.startswith('linux'):
        print("\n[!] Unsupported platform.")
        print("\nExiting program ...\n")
        exit(1)

    args = parse_args()

    network_option = args.network
    vpn_country = args.country
    user_agent_host = args.user_agent

    # TODO
    # countries = {
    #     "SK" : "Slovakia",
    #     "FR" : "France",
    #     "US" : "United_States",
    # }

    if network_option == "VPN":
        if vpn_country == "SK":
            vpn_country = "Slovakia"
        elif vpn_country == "FR":
            vpn_country = "France"
        elif vpn_country == "US":
            vpn_country = "United States"
        else:
            # defaulting to France
            vpn_country = "France"

    verbosity = args.verbosity

    web_collector = initialize_collector(
        network_option, vpn_country, user_agent_host, verbosity)

    initialize_network(web_collector, network_option, vpn_country)

    url = args.url

    if not args.check:
        initialize_driver(web_collector)
        start_crawling(web_collector, url)
        destroy_drive(web_collector)
    else:
        start_checking(web_collector, url)

    stop_network(web_collector, network_option)


if __name__ == '__main__':
    main()
