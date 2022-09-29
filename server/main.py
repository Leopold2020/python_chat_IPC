#Oskar Svedlund & Oliver stafferod
#TEINF-20
#2022-09-23
#Internal Python Chat projekt

# Not working

import socket
from threading import Thread
from resources import listen_for_client

Server_host = "0.0.0.0"
Server_port = 5002
client_sockets = set()
Separator_token = "<SEP>"


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((Server_host, Server_port))
s.listen(5)

print(f"[...] Listening as {Server_host}:{Server_port}")

while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()
