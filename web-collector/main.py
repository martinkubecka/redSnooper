import platform
import argparse
from colorama import Fore

from initialize import start
from initialize import stop


###################################################
## url                                           ##
###################################################
## network_option                                ##
## -- MOBILE_DATA                                ##
## -- VPN                                        ##
## -- TOR                                        ##
###################################################
## vpn_country                                   ##
## -- Slovakia                                   ##
## -- France                                     ##
## -- United_States                              ##
#  -- None (if not network_option == VPN)        ##
###################################################
## user_agent_host                               ##
## -- Desktop                                    ##
## -- Android                                    ##
## -- iOS                                        ##
###################################################
## verbosity                                     ##
## -- level [0/1]                                ##
###################################################

# WEBHOOK : https://webhook.site/75d7b590-e9e9-4554-a483-99cc8fa7eb6d


def banner():
    print(f"""
{Fore.RED}             _ {Fore.RESET}_____      |                 
{Fore.RED}   ___ ___ _| |{Fore.RESET}   __|___ _|_ ___ ___ ___ ___ 
{Fore.RED}  |  _| -_| . |{Fore.RESET}__   | ---[o]--- | . | -_|  _|
{Fore.RED}  |_| |___|___|{Fore.RESET}_____|_|_|_|_|___|  _|___|_|  
                          |     |_|          
    """)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Redirect chain analysis tool with random user agents supporting VPN and TOR as a network configuration')

    parser.add_argument('-u', '--url', metavar="URL", required=True,
                        help='URL for analysis (use double quotes)')
    parser.add_argument('-n', '--network', metavar="OPTION", default="MOBILE",
                        help='network configuration option [MOBILE/VPN/TOR] (default: MOBILE)')
    parser.add_argument('-c', '--country', metavar="COUNTRY", default="France",
                        help='VPN country [SK/FR/US] (required if VPN is selected)')
    parser.add_argument('-a', '--user-agent', metavar="OPTION", default="Desktop",
                        help='user agent [Desktop/Android/iOS] (default: Desktop)')
    parser.add_argument('-v', '--verbosity', metavar="LEVEL", default="0",
                        help='redirect chain verbosity [0/1] (default: 0)')

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

    if network_option == "MOBILE":
        network_option = "MOBILE_DATA"

    if network_option == "VPN":
        if vpn_country == "SK":
            vpn_country = "Slovakia"
        elif vpn_country == "FR":
            vpn_country = "France"
        elif vpn_country == "US":
            vpn_country = "United_States"
        else:
            # defaulting to France
            vpn_country = "France"

    verbosity = args.verbosity

    web_collector = start(network_option, vpn_country,
                          user_agent_host, verbosity)

    url = args.url
    web_collector.crawl(url)

    stop(web_collector, network_option)


if __name__ == '__main__':
    main()
