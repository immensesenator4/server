import os
from sock import Socket
import socket
Info:dict[str,str] ={}
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

            with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        if ("Recieve" in f"{data!r}" ):
                                isVar=False
                                var=""
                                count=0
                                for i in f"{data!r}":
                                    if isVar:
                                        var+=i
                                    elif i == ":":
                                        isVar=not isVar
                                    
                                var=var.replace("'","")
                                conn.sendall(Info[var])
                              

                        else:
                            var=""
                            count=0
                            for i in f"{data!r}":
                                if count==0:
                                    pass
                                elif i == ":":
                                    break
                                else:
                                    var+=i
                                count+=1
                            var.replace("'","")
                            count = len(var)+1
                            new_data=""
                            for char in f"{data!r}":
                                if count<0:
                                    new_data+=char
                                count-=1
                            var=var.replace("'","")
                            Info[var]= new_data.encode()
                    print(Info)
            s.close()
    except Exception as e:
        print(e)
        time.sleep(3)