import socket
import json
import os
import ast
import types

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
    def send_str(self,var,contents):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"{var}={contents}".encode())
            return s.recv(1024)
    def send_int(self,var,contents:int):
        y = json.dumps(contents)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"{var}={y}".encode())
            return s.recv(1024)
    def send_obj(self,var:str,contents:object):
        y = json.dumps(contents.__dict__)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"{var}={y}".encode())
            return s.recv(1024)
    def recieve_str(self,var):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
            s.connect((self.host, self.port)) 
            s.sendall(f"{var}=recieve".encode())
            return s.recv(1024)
    def recieve_int(self,var):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
            s.connect((self.host, self.port)) 
            s.sendall(f"{var}=recieve".encode())
            return int(s.recv(1024).decode()[0:-1])
    def receive_obj(self,var,new_var:object):
        def alter__init__(self,new_dict:dict):
             for key, value in new_dict.items():

                setattr(self, key, value) 
        funcType = types.MethodType
        new_var.__init__=funcType(alter__init__,new_var)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
            s.connect((self.host, self.port)) 
            s.sendall(f"{var}=recieve".encode())
            class_param=s.recv(1024).decode()
            class_param=ast.literal_eval(class_param[0:-1])
            new_var.__init__(class_param)
            return new_var
    def comunicate(self,content:str):
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
            s.connect((self.host, self.port)) 
            s.sendall(content.encode())
            return s.recv(1024)
d=client("10.1.40.194",13455 )

d.send_int("need",37787)
z=d.recieve_int("need")
print(z)