# FROM python:3.7-alpine3.14
FROM python:3.10.8-alpine3.16

WORKDIR /app/

# add /app to $PATH to run 'geckodriver' from the cwd 
ENV PATH="${PATH}:/app"

# install required tools
RUN python -m pip install --upgrade pip
RUN apk add --no-cache unzip
RUN apk add --no-cache vim
RUN apk add --no-cach wget
RUN apk add --no-cach curl
RUN apk add --no-cach tor
RUN apk add --no-cache gcc g++ make musl-dev python3-dev libxslt-dev libxml2-dev libffi-dev

# install app requirements
RUN apk add --no-cache firefox
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz -O geckodriver.tar.gz && tar -xzf geckodriver.tar.gz && rm -f geckodriver.tar.gz
RUN pip install flask
RUN pip install flask-cors
RUN pip install selenium-wire
RUN pip install random_user_agent
RUN pip install requests
RUN pip install stem
RUN pip install PyYAML

# install OpenVPN
RUN apk add openvpn
RUN wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip
RUN unzip ovpn.zip
RUN rm ovpn.zip

# configure auto auth for OpenVPN
COPY ./vpn_login.txt /app/vpn_login.txt
RUN cp vpn_login.txt ovpn_udp/
RUN cp vpn_login.txt ovpn_tcp/
RUN find ovpn_udp/ -type f -name "*nordvpn.com.udp.ovpn" -print0 | xargs -0 sed -i 's+auth-user-pass+auth-user-pass /app/ovpn_udp/vpn_login.txt+'
RUN find ovpn_tcp/ -type f -name "*nordvpn.com.tcp.ovpn" -print0 | xargs -0 sed -i 's+auth-user-pass+auth-user-pass /app/ovpn_tcp/vpn_login.txt+'
RUN rm vpn_login.txt

COPY ./initialize.py /app/initialize.py
COPY ./.config.yml /app/.config.yml
COPY ./tor_runner.py /app/tor_runner.py
COPY ./vpn_servers.json /app/vpn_servers.json
COPY ./web_collector.py /app/web_collector.py
COPY ./server.py /app/server.py


EXPOSE 3000

ENTRYPOINT ["python"]
CMD ["/app/server.py"]