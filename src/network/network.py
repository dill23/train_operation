import threading as th
import socket as st

PORT = 34197
SERVER = st.gethostbyname(st.gethostname)
ADDR = (PORT, SERVER)

server = st.socket(st.AF_INET, st.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    pass

def start():
    server.listen()
    connect = True
    while connect:
        conn, addr = server.accept()
        

start()
