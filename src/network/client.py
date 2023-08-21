import socket as st

HEADER = 64
PORT = 5050
FORMAT ='UTF-8'
SERVER = st.gethostbyname(st.gethostname())
DISCONNECT_MESSEGE = '!disconect'
ADDR = (SERVER, PORT)

client = st.socket(st.AF_INET, st.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("hello")