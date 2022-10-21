import time
from sys import platform
from web_collector import ENTITY_WEB_COLLECTOR


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


def start(network_option, vpn_country, user_agent_host):
    web_collector = ENTITY_WEB_COLLECTOR(
        network_option, user_agent_host, vpn_country)
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

    # NOTE : Checking IP after terminating TOR results to ERROR while fetching the current IP
    if network_option == "VPN":
        web_collector.check_ip()

def banner():
    print(r"""
             _ _____      |                 
   ___ ___ _| |   __|___ _|_ ___ ___ ___ ___ 
  |  _| -_| . |__   | ---[o]--- | . | -_|  _|
  |_| |___|___|_____|_|_|_|_|___|  _|___|_|  
                          |     |_|          
    """)

####################################################################################
####################################################################################
####################################################################################
# TESTING outside of Docker container
# -- CHECKLIST
# [1] UNCOMMENT 'kill' COMMANDS IN 'stop_network()'
# [2] UNCOMMENT 'webdriver.Firefox' in 'initialize_driver()'


# def testing(network_option=None, user_agent_host=None, vpn_country=None):

#     if not platform.startswith('linux'):
#         print("\n[!] Unsupported platform.")
#         print("\nExiting program ...\n")
#         exit(1)

#     print("-------------------------------------------------------------------------")

#     # [0] = "MOBILE_DATA" | [1] = "VPN" | [2] = "TOR"
#     network_options = ["MOBILE_DATA", "VPN", "TOR"]
#     network_option = network_options[1]

#     # TODO : user will choose specific USER AGENT host
#     user_agent_host = "Desktop"

#     # if VPN is not selected 'vpn_country = None'
#     # TODO : user will choose specific country (SK, FR, US) when VPN is selected
#     vpn_country = "France"

#     web_collector = ENTITY_WEB_COLLECTOR(
#         network_option, user_agent_host, vpn_country)
#     web_collector.initialize_network()
#     time.sleep(5)

#     current_country = web_collector.check_ip()
#     # TODO : REWORK !!!
#     if network_option == "VPN":
#         if not vpn_country == "Slovakia" and current_country == "Slovakia":
#             print(
#                 f"[!] With definied parameters current country should not be Slovakia\n")
#             while not current_country == "Slovakia":
#                 current_country = web_collector.check_ip()

#     web_collector.initialize_driver()
#     web_collector.crawl(
#         "https://webhook.site/23233635-6f3f-4775-926e-f5d36881a269")
#     web_collector.destroy_driver()

#     print("-------------------------------------------------------------------------")

#     # TODO : rework based on the frontend requirements
#     web_collector.stop_network()
#     time.sleep(5)
#     # NOTE : Checking IP after terminating TOR results to error while fetching current IP
#     if network_option == "VPN":
#         web_collector.check_ip()

#     return web_collector


# def main():
#     testing()


# if __name__ == '__main__':
#     main()
