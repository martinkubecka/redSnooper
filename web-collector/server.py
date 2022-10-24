from flask import Flask, jsonify, request, send_from_directory, send_file
from flask_cors import CORS
from web_collector import ENTITY_WEB_COLLECTOR
import json
import sys

from initialize import start
from initialize import stop

app = Flask(__name__)
CORS(app)


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

@app.route('/status', methods=['GET'])
def status():
    return 'I LIVE'

# -------------------------------------- TESTING --------------------------------------
@app.route('/test', methods=['GET'])
def test_crawl():
    network_option = "MOBILE_DATA"
    # network_option = "VPN"
    # network_option = "TOR"
    vpn_country = "Slovakia"
    user_agent_host = "Desktop"
    verbosity = 0
    web_collector = start(network_option, vpn_country,
                          user_agent_host, verbosity)
    url = "https://webhook.site/75d7b590-e9e9-4554-a483-99cc8fa7eb6d"
    web_collector.crawl(url)
    stop(web_collector, network_option)
    return "TEST DONE"
# -------------------------------------------------------------------------------------


# @app.route('/control', methods=['GET'])
# def control():
#     return '''
#     <html>
#         <head>
#             <title>HECATONCHEIRES</title>
#             <script>
#                 function crawl() {
#                     stat = document.getElementById('status_bar');
#                     stat.style.backgroundColor = 'yellow';
#                     stat.innerHTML = 'REQUEST SEND. WAIT';
#                     var xhttp = new XMLHttpRequest();
#                     xhttp.open("POST", "http://localhost:3000/crawl", true);
#                     xhttp.setRequestHeader("Content-Type", "application/json");
#                     xhttp.onreadystatechange = function() {
#                         if (this.readyState == 4 && this.status == 200) {
#                             stat.style.backgroundColor = 'green';
#                             stat.innerHTML = 'RZLT OK. READY';
#                             var data = JSON.parse(this.responseText);
#                             console.log(data);
#                             document.getElementById('rzlt').value = this.responseText;
#                         }
#                         else {
#                             stat.style.backgroundColor = 'red';
#                             stat.innerHTML = 'ERROR NO RESPONSE'
#                         }
#                     };
#                     var formData = new FormData();
#                 	formData.append('url', document.getElementById('url').value);
#                     xhttp.send(JSON.stringify({'url':document.getElementById('url').value, 'selector':document.getElementById('selector').value}));
#                 }
#             </script>
#         </head>
#         <body>
#             <center>
#                 <p id="status_bar" style="background-color: green;">READY</p>
#                 <h4>URL</h4>
#                 <input id="url" style="width:100%;">
#                 <p>
#                     <button onclick="crawl();">CRAWL IT</button>
#                 </p>
#                 <h4>RZLT</h4>
#                 <textarea id="rzlt" style="width:100%;height: 300px;"></textarea>
#             </center>
#         </body>
#     </html>
#     '''


# @app.route('/crawl', methods=['POST'])
# def tarang():
#     if request.method == 'POST':
#         data = json.loads(request.data)
#         url = data['url']
#         data = web_collector.crawl(url)
#         if data is not None:
#             return json.dumps(data)
#         else:
#             return json.dumps(['CRAWLING ERROR'])

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=3000, debug=False, use_reloader=False)    # do not reload because VPN or TOR is 2x initialized
    app.run(host='0.0.0.0', port=3000, debug=False, use_reloader=False)
