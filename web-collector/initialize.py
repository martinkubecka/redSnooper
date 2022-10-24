import time
from sys import platform
from web_collector import ENTITY_WEB_COLLECTOR


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


def start(network_option, vpn_country, user_agent_host, verbosity):
    web_collector = ENTITY_WEB_COLLECTOR(
        network_option, user_agent_host, vpn_country, verbosity)
    web_collector.initialize_network()
    time.sleep(5)

    current_country = web_collector.check_ip()

    # NOTE : MAY CAUSE SOME PROBLEMS ...  LEVEL PARANOID
    if network_option == "VPN":
        if not vpn_country == "Slovakia" and current_country == "Slovakia":
            print(
                f"[!] With definied parameters current country should not be Slovakia\n")
            while not current_country == "Slovakia":
                current_country = web_collector.check_ip()

    web_collector.initialize_driver()

    return web_collector


def stop(web_collector, network_option):
    web_collector.destroy_driver()

    # TODO : rework based on the frontend requirements
    web_collector.stop_network()
    time.sleep(5)

    if network_option == "VPN":
        web_collector.check_ip()