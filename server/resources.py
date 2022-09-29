#Oskar Svedlund & Oliver stafferod
#TEINF-20
#2022-09-23
#Internal Python Chat projekt

import socket
from threading import Thread

client_sockets = set()
Separator_token = "<SEP>"


def listen_for_client(cs):
     while True:
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()
        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            # if we received a message, replace the <SEP> 
            # token with ": " for nice printing
            msg = msg.replace(Separator_token, ": ")