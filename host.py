import socket
import json
import os
import ast
class Host(object):
    def __init__(self,size:int,port:int):
            self.port=port
            self.hostname = socket.gethostname()
            # self.ip_address = socket.gethostbyname(self.hostname)     
            self.ip_address='0.0.0.0'       
            self.data={}
            self.var=[]
            self.size=size
            self.adresses=[]
            self.record=[]
    def get_person(self):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.ip_address, self.port))
                s.listen()
                conn, addr = s.accept()

                if addr[0] not in self.adresses and len(self.adresses)+1<=self.size:
                     self.adresses.append(addr[0])
                     self.record.append(0)
                if addr[0] in self.adresses:
                    
                    for i in range(0,len(self.adresses)):
                        self.record[i]+=1
                        if addr[0]== self.adresses[i]:
                            self.record[i]=0
                        elif self.record[i]==10:
                            self.record.pop(i)
                            self.adresses.pop(i)
                            break
                    os.system('cls')
                    for adr in self.adresses:
                        print(f"{adr} is conected to network")
                    with conn:
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                break
                            if ("recieve" in f"{data!r}" ):
                                var=""
                                count=0
                                for i in f"{data!r}":
                                    if count==0:
                                        pass
                                    elif i == "=":
                                        break
                                    else:
                                        var+=i
                                    count+=1
                                
                                    
                                if var in self.var:
                                    self.send(self.data[var],conn)
                                else:
                                    self.send(b'N/a',conn)
                            elif "hi"in f"{data!r}":
                                self.send("available".encode(),conn)
                            else:
                                var=""
                                count=0
                                for i in f"{data!r}":
                                    if count==0:
                                        pass
                                    elif i == "=":
                                        break
                                    else:
                                        var+=i
                                    count+=1
                                self.var.append(var)
                                count = len(var)+1
                                new_data=""
                                for char in f"{data!r}":
                                    if count<0:
                                        new_data+=char
                                    count-=1
                                self.data[var]= new_data.encode()
                                self.send(b'recieved',conn)
                            return data,addr
                else:
                    self.send(b"server not found",conn)
    def comunicate(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.ip_address, self.port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print(f"{data!r}")
                        l=input("respond")
                        self.send(l.encode(),conn)
                        os.system('cls')
    def send(self,data:bytes,conn):
        conn.sendall(data)

h=Host(2,13455)

while True:
    h.get_person()