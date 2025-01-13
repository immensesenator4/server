import socket
import json
import os
#type will be stored in the future so we can transmute integers and booleans and lists
# this will happen when client class is made
#what is below is a send and recieve function
#this will continue with a self.host and self. ip adress which i would have to make somethingto search the port i think
HOST =  "192.168.12.195" 
PORT = 13455 
class client(object):
    def __init__(self,host,port):
        self.host=host
        self.port = port
    def send(self,var,contents):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"{var}={contents}".encode())
            return s.recv(1024)
    def recieve(self,var):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
            s.connect((self.host, self.port)) 
            s.sendall(f"{var}=recieve".encode())
            return s.recv(1024)
    def comunicate(self,content:str):
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
            s.connect((self.host, self.port)) 
            s.sendall(content.encode())
            return s.recv(1024)
d=client("10.1.40.194",13455 )
me =str(3222222)
# d.send("player",me)
# print(f"Received {d.recieve("player")!r}")
# me=(d.recieve("player").decode())
# print(me)
while True:
    ne=input("message\n")
    f=d.comunicate(ne)
    os.system('cls')
    print(f"host {d!r}")
