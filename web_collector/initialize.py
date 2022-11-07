import time

from web_collector.web_collector import WebCollector


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
    if network_option == "VPN":
        if not vpn_country == "Slovakia" and current_country == "Slovakia":
            print(
                f"[!] With definied parameters current country should not be Slovakia\n")
            while not current_country == "Slovakia":
                current_country = web_collector.check_ip()


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
