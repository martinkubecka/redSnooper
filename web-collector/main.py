import platform
import argparse


from web_collector import ENTITY_WEB_COLLECTOR
from initialize import banner
from initialize import start
from initialize import stop


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

def parse_args():
    parser = argparse.ArgumentParser(description='redSnooper')

    parser.add_argument('-n', '--network', metavar="OPTION", default="MOBILE",
                        help='network configuration option [MOBILE/VPN/TOR] (default: MOBILE)')
    parser.add_argument('-c', '--country', metavar="COUNTRY", default="France",
                        help='VPN country [SK/FR/US] (required if VPN is selected)')
    parser.add_argument('-u', '--user-agent', metavar="OPTION", default="Desktop",
                        help='user agent [Desktop/Android/iOS] (default: Desktop)')

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
            print(f"[!] Invalid country was selected for the VPN server")
            print(f"[*] Defaulting to 'France'")

    web_collector = start(network_option, vpn_country, user_agent_host)

    web_collector.crawl(
        "https://webhook.site/68370783-ead5-4adc-90de-279324b5c9e3")

    stop(web_collector, network_option)


if __name__ == '__main__':
    main()
