from sock import Socket
import socket
import json
import os
os.system("title openServer")
r=""
try:
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1",2))
    s=sock.recv(1024)
    s=json.loads(s.decode())
    r=sock.recv(1024).decode()
    sock.close()
except Exception as e:
    print(e)
    s=0

newUdp = Socket(r,int(s))
print("hi")
try:
    newUdp.listen()
except Exception as e:
    print(e)
