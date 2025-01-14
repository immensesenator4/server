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
    def __init__(self):
        self.host,self.port= self.find_servers(end_port=99)
    def send_str(self,var:str,contents):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"{var}={contents}".encode())
            return s.recv(1024)
    def send_int(self,var:str,contents:int):
        y = json.dumps(contents)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"{var}={y}".encode())
            return s.recv(1024)
    def send_bool(self,var:str,contents:bool):
        y = json.dumps(contents)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"{var}={y}".encode())
            return s.recv(1024)
    def send_dict(self,var:str,contents:dict):
        y = json.dumps(contents)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"{var}={y}".encode())
            return s.recv(1024)
    def send_list(self,var:str,contents:list):
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
    def recieve_str(self,var:str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
            s.connect((self.host, self.port)) 
            s.sendall(f"{var}=recieve".encode())
            return s.recv(1024)
    def recieve_int(self,var:str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
            s.connect((self.host, self.port)) 
            s.sendall(f"{var}=recieve".encode())
            return int(s.recv(1024).decode()[0:-1])
    def recieve_bool(self,var:str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
            s.connect((self.host, self.port)) 
            s.sendall(f"{var}=recieve".encode())
            new_bool=s.recv(1024).decode()
            return ("true"in new_bool.lower())
    def recieve_dict(self,var:str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
            s.connect((self.host, self.port)) 
            s.sendall(f"{var}=recieve".encode())
            new_dict=s.recv(1024).decode()
            new_dict=ast.literal_eval(new_dict[0:-1])
            
            return new_dict
    def recieve_list(self,var:str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
            s.connect((self.host, self.port)) 
            s.sendall(f"{var}=recieve".encode())
            return json.loads(s.recv(1024).decode()[0:-1])
    def receive_obj(self,var:str,new_var:object):
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
    def scan_port(self,ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.000000000000000000000000001)  # Timeout after 1 second
                s.connect((ip, port))
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False

    def find_servers(self, start_port=1, end_port=9999):
        net_ip= self.simplify_ip()
        for port in range(start_port, end_port + 1):
            for i in range(1, 255):
                ip = f"{net_ip}.{i}"
                if self.scan_port(ip, port):
                    print(f"Server found at {ip}:{port}")
                    return ip,port
    def simplify_ip(self):
        ip=""
        net_ip=""
        count=0
        for char in socket.gethostbyname(socket.gethostname()):
            if char==".":
                count+=1
                net_ip=ip
            if count==3:
                return net_ip
            else:
                ip+=char
            

d=client()
d.send_list("me",["dre","re",2,3,4,5])
z=d.recieve_list("me")
print(z)