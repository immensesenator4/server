import random as r
import socket
import json
import os
import ast
import time
from typing import overload
class Socket(object):
    
    
    def __init__(self,reason:str="None",port:int=0,ip:str=socket.gethostbyname(socket.gethostname())):
        abcs=r"qwertuiopasdfghklzxcvbnm12345890[]\|';/.,!@#$%^&*()_-=`~"
        self.callId=""
        self.sock = None
        self.ip=ip
        self.port =port
        for i in range(0,r.randint(7,38)):
            e=r.randint(0,len(abcs)-1)
            self.callId+=abcs[e]
           
        self.reason=reason
    def recieve(self):
        return self.sock.recv(1024).decode()
    def uncompress(self,data):
        return json.loads(data)
    def getServers(self):
        ips=[]
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        server_address = ('', self.port) 
        sock.bind(server_address)


        while len(ips)<1:
            data, address = sock.recvfrom(1024)  
            print(f"Received message: {data.decode()} from {address}")
            if self.reason == data.decode()and address[0] not in ips:
                ips.append(address[0])
        sock.close()
        return ips

    def listen(self):
        

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        message = f"{self.reason}".encode()
        while True:
            sock.sendto(message, ('<broadcast>', self.port))
           
                
            time.sleep(2)  
        s.close()
        sock.close()

    def sendFile(self,File:str):
        f=open(File,"rb")
        data=f.read(1024)
        while data:
            self.sock.send(data)
            data=f.read(1024)
        self.sock.send("$$".encode())
        f.close()
    def recieveFile(self,conn:socket.socket):
        f=""
        while True:
            try:
                data= conn.recv(1024).decode()
                if "$$" in data:
                    break
                f+=data
            except:
                break
        return f
    def ServerClose(self):
        self.sock.sendto("shutdown",(("127.0.0.1",self.port)))
        self.sock.shutdown(2)
    def simplify_name_func(self,obj:str):
        shortened_name=''
        for i in obj:
            if i ==' ':
                break
            elif "<":
                pass
            else:
                shortened_name+=i
        return shortened_name
    def simplify(self,obj:dict|list, is_dict:bool=True)->dict|list:
        excludables=(int,str,float,dict,list,tuple,bool,bytes)
        
        if is_dict:
            ran=False
            deep_coppy={}
            

            for key,var in obj.items():
                ran=True
                if isinstance(var,excludables):
                    if isinstance(var,list):
                        is_items = len(var)>0
                        if is_items:
                            z= self.simplify(var,False)
                        else:
                            z= var

                    elif isinstance(var,dict):
                        is_items = len(var)>0
                        z= self.simplify(var)
                    else:
                        z= var
                else:
                    try:
                        obj_dict=var.__dict__
                        obj_dict['object']=self.simplify_name_func(str(obj))
                        z= self.simplify(obj_dict)
                    except:
                        z= key
                deep_coppy[key]=z
            
            return deep_coppy
            
        elif isinstance(obj,list):
            deep_coppy=[]
            for i in range(0,len(obj)):
                var=obj[i]
                if isinstance(var,excludables):
                    if isinstance(var,list):
                        is_items = len(var)>0
                        
                        if is_items:
                            z= self.simplify(var,False)
                        else:
                            z= var
                    elif isinstance(var,dict):
                        is_items = len(var)>0
                    
                        if is_items:
                            z= self.simplify(var,False)
                        else:
                            z= var
                    else:
                        z= var
                else:
                    try:
                        obj_dict=var.__dict__
                        obj_dict['object']= self.simplify_name_func(str(var))
                        z= self.simplify(obj_dict)
                    except:
                        z= obj[i]
                deep_coppy.append(z)
            
        
        return deep_coppy
    def compressFile(self,File:str):
        fileText=""
        with open(os.getcwd()+"\\"+File,"r+")as f:
            fileText=f.read()
        return self.compress(fileText)

    def compress(self,data):
        return json.dumps(data)
    def compressObj(self,obj:object,):
        new=obj.__dict__.copy()
        z:dict=self.simplify(new)
        
        y = json.dumps(z)
        return y
    def connectServer(self,ip:str,port:int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip,port))
    def Disconect(self):
        self.sock.close()
    
    def send(self,data:str):
        self.sock.send(data.encode())
    def host(self,hostFile:str=f"\\Udphost.py"):
        os.system(f"start cmd.exe /c python {os.getcwd()}{hostFile}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1",2))
            s.listen()
            conn, literal= s.accept()
            conn.sendall(json.dumps(self.port).encode())
        self.sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        h.sock.bind((self.ip,self.port))

if __name__ == "__main__":
    h=Socket("testForPython",22)
    # print("why")
    h.host()
    s=None
    while not s:
        h.sock.listen()
        conn,addr = h.sock.accept()
        try:
            data = h.recieveFile(conn)
            print("from "+str(addr) + " recieved " +data)
            s=data
        except Exception as e:
            print(e)
    h.ServerClose()
