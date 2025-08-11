import os
from sock import Socket
import socket
Info:dict ={}
import json
import time
os.system("title echoServer")
r="testForPython"
try:
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1",2))
    s=sock.recv(1024)
    s=json.loads(s.decode())
    r=sock.recv(1024).decode()
    sock.close()
except Exception as e:
    print(e)
    s=22
try:
    newTCP = Socket(r,int(s))
    print("hi")
except Exception as e:
    print(e)
    newTCP = Socket(r,int(s))
try:
    newTCP.host(isEcho=False)
except Exception as e:
    print(e)

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((newTCP.ip,newTCP.port))
            s.listen()
            conn, literal= s.accept()
            n=conn.recv(1024)
            if n.decode()[0:4] == "send":
                print(True)
            print(n.decode())
            s.close()
    except Exception as e:
        print(e)
        time.sleep(3)