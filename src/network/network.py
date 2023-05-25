import threading as th
import socket as st

HEADER = 64
PORT = 34197
SERVER = st.gethostbyname(st.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSEGE = '!disconect'

server = st.socket(st.AF_INET, st.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[new connection] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSEGE:
                connected = False
            print(f"{addr}: {msg}")
    conn.close()

def start():
    print("started")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = th.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start()
