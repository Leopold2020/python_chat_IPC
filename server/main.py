#Oskar Svedlund & Oliver stafferod
#TEINF-20
#2022-09-23
#Internal Python Chat projekt

import socket
from threading import Thread
from resources import listen_for_client

Server_host = "0.0.0.0"
Server_port = 5002


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((Server_host, Server_port))
s.listen(5)

print(f"[...] Listening as {Server_host}:{Server_port}")