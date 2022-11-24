import os
import sys
import time
import platform
import argparse
import logging
from colorama import Fore

from webcollector.web_collector import WebCollector


def initialize_collector(network_option, vpn_country, user_agent_host, verbosity):
    web_collector = WebCollector(
        network_option, user_agent_host, vpn_country, verbosity)
    return web_collector


def initialize_driver(web_collector):
    web_collector.initialize_driver()


def initialize_network(web_collector, network_option, vpn_country):
    web_collector.initialize_network()
    time.sleep(5)

    current_country = web_collector.check_ip()

    # NOTE : MAY CAUSE SOME PROBLEMS ... SHOULD BE REWORKED
    # if network_option == "VPN":
    #     if not vpn_country == "Slovakia" and current_country == "Slovakia":
    #         print(
    #             f"[{time.strftime('%H:%M:%S')}] [WARNING]  With definied parameters current country should not be Slovakia")
    #         logging.warning(
    #             "With definied parameters current country should not be Slovakia")
            # while not current_country == "Slovakia":
            #     current_country = web_collector.check_ip()


def start_checking(web_collector, url):
    web_collector.check(url)


def start_crawling(web_collector, url):
    web_collector.crawl(url)


def destroy_drive(web_collector):
    web_collector.destroy_driver()


def stop_network(web_collector, network_option):
    web_collector.stop_network()
    time.sleep(5)

    if network_option == "VPN":
        web_collector.check_ip()


def banner():
    print(f"""
{Fore.RED}             _ {Fore.RESET}_____      |                 
{Fore.RED}   ___ ___ _| |{Fore.RESET}   __|___ _|_ ___ ___ ___ ___ 
{Fore.RED}  |  _| -_| . |{Fore.RESET}__   | ---[o]--- | . | -_|  _|
{Fore.RED}  |_| |___|___|{Fore.RESET}_____|_|_|_|_|___|  _|___|_|  
                          |     |_|          
    """)


def arg_formatter():
    def formatter(prog): return argparse.HelpFormatter(
        prog, max_help_position=52)
    return formatter


def parse_args():
    parser = argparse.ArgumentParser(formatter_class=arg_formatter(),
                                     description='Redirect chain analysis tool with random user agents supporting VPN and TOR as a network configuration.')

    parser.add_argument('-u', '--url', metavar="URL", required=True,
                        help='URL for analysis (use double quotes)')
    parser.add_argument(
        '-q', '--quiet', help="do not print banner", action='store_true')
    parser.add_argument('-n', '--network', metavar="OPTION", default="MOBILE",
                        help='network configuration option [MOBILE/VPN/TOR] (default: MOBILE)')
    parser.add_argument('-c', '--country', metavar="COUNTRY", default="France",
                        help='VPN country [SK/FR/US] (required if VPN is selected)')
    parser.add_argument('-a', '--user-agent', metavar="OPTION", default="Desktop",
                        help='user agent [Desktop/Android/iOS] (default: Desktop)')
    parser.add_argument('-v', '--verbosity', metavar="LEVEL", default="0",
                        help='redirect chain verbosity [0/1] (default: 0)')
    parser.add_argument('--check', action='store_true',
                        help='check if the provided URL is active')

    return parser.parse_args(args=None if sys.argv[1:] else ['--help'])


def check_report_directory(output_dir):
    report_dir = f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/reports"

    if output_dir == "reports":
        report_dir = f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/reports"
    else:
        report_dir = output_dir

    if not os.path.isdir(report_dir):
        print(
            f"[{time.strftime('%H:%M:%S')}] [INFO] Creating '{report_dir}' for storing analysis reports")
        logging.info(f"Creating '{report_dir}' for storing analysis reports")
        os.mkdir(report_dir)

def init_logger():
    logging_path = f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/logs"
    if not os.path.isdir(logging_path):
        os.mkdir(logging_path)
    logging.basicConfig(format='%(created)f; %(asctime)s; %(levelname)s; %(name)s; %(message)s',
                        filename=f"{logging_path}/{(os.path.splitext(__file__)[0]).split('/')[-1]}.log", level=logging.DEBUG)
    return logging.getLogger('__name__')


def main():
    print("\033[H\033[J", end="")
    logger = init_logger()
    check_report_directory("reports")

    machine_platfrom = platform.system().lower()
    if not machine_platfrom.startswith('linux'):
        print(f"[{time.strftime('%H:%M:%S')}] [ERROR] Unsupported platform")
        logging.error("Unsupported platform")
        print("\nExiting program ...\n")
        exit(1)

    args = parse_args()

    if not args.quiet:
        banner()

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
