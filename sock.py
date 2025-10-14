import random as r
import socket
import json
import os
import ast
import time
import types
from typing import overload
import subprocess
class Socket(object):
    def __init__(self,reason:str="None",port:int=0,ip:str=socket.gethostbyname(socket.gethostname())):
        abcs=r"qwertuiopasdfghklzxcvbnm12345890[]\|';/.,!@#$%^&*()_-=`~"
        self.callId:str=""
        self.sock:socket.socket = None
        self.ip:str=ip
        self.port:int =port
        self.HostList:dict[str,subprocess.Popen]={}
        for i in range(0,r.randint(7,38)):
            e=r.randint(0,len(abcs)-1)
            self.callId+=abcs[e]
        self.reason:str=reason
    def decompress_obj(self,obj,newvar,objects={})->object:
        return self.Reasign(obj,newvar,objects)
    def setCallId(self,id:str):
        self.callId =id
    def uncompileobjs(self,obj:dict|list,objects:dict={})->dict|list:
        if isinstance(obj,(dict)):
            for key, value in obj.items():
                if isinstance(value,(dict)):
                    if "object" in value.keys():
                        z=self.Reasign(value,objects[value["object"]],objects)
                    else:
                        z=self.uncompileobjs(value,objects)

                elif key == "object":
                    pass
                elif isinstance(value,(list)):
                    z=self.uncompileobjs(value,objects)
                else:
                    z=value
                try:
                    obj[key]=z
                except:
                    pass
        elif isinstance(obj,(list)):
            for i in range(0,len(obj)):
                if isinstance(obj[i],(dict)):
                    if "object" in obj[i].keys():
                        z=self.Reasign(obj[i],objects[obj[i]["object"]],objects)
                    else:
                        z=self.uncompileobjs(obj[i],objects)

                elif key == "object":
                    pass
                elif isinstance(obj[i],(list)):
                    z=self.uncompileobjs(obj[i],objects)
                else:
                    z=obj[i]
                try:
                    obj[i]=z
                except:
                    pass
            pass
        return obj
    def Reasign(self,obj:dict,newVar:object,objects:dict={})->object:
        def alter__init__(self,new_dict:dict,Reasign=self.Reasign,uncompiledobjs=self.uncompileobjs,objects:dict={}):
             for key, value in new_dict.items():
                if isinstance(value,(list,dict)):
                    if isinstance(value,(list)):
                        z=uncompiledobjs(value,objects)
                    else:
                        if "object" in value.keys():
                            z=Reasign(value,objects[value["object"]],objects)
                        else:
                            z=uncompiledobjs(value,objects)
                    setattr(self,key,z)
                else:    
                    setattr(self, key, value) 
        funcType = types.MethodType
        newVar.__init__=funcType(alter__init__,newVar)
        newVar.__init__(obj,objects=objects)
        return newVar
    def recieve(self,conn:socket.socket=None)->str:
        if conn:
            return conn.recv(1024).decode()
        else:
            return self.sock.recv(1024).decode()
    def uncompress(self,data)->any:
        return json.loads(data)
    def getServers(self,limitTime:int = 5,ServerCount:int=99999):
        ips=[]
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        server_address = ('', self.port) 
        sock.bind(server_address)
        s=time.time()

        while len(ips)<ServerCount or time.time()-s<limitTime:
            data, address = sock.recvfrom(1024)  
            # print(f"Received message: {data.decode()} from {address}")
            if self.reason == data.decode()and address[0] not in ips:
                ips.append(address[0])
        sock.close()
        return ips

    def listen(self):
        

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        n=True
        message = f"{self.reason}".encode()
        while n:
            sock.sendto(message, ('<broadcast>', self.port))
           
                
            time.sleep(2)  
        sock.close()

    def simplify_name_func(self,obj:str)->str:
        shortened_name=''
        for i in obj:
            if 'object'in shortened_name:
                shortened_name=shortened_name[0:-6]
                break
            elif "<" == i:
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
    def compressFile(self,File:str)->str:
        fileText:str=""
        with open(os.getcwd()+"\\"+File,"r+")as f:
            fileText=f.read()
        fileText+="$$"
        return self.compress(fileText)

    def compress(self,data):
        return json.dumps(data)
    def compressObj(self,obj:object,):
        new=obj.__dict__.copy()
        z:dict=self.simplify(new)
        
        y = json.dumps(z)
        return y
    def ClientConnect(self,ip:str,port:int):
        self.ip=ip
        self.port=port
    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.ip,self.port))
        except:
            pass
    def Disconect(self):
        self.sock.close()

    def send(self,data:str,conn:socket.socket=None):
        if conn:
            conn.sendall(data.encode())
        else:
            self.sock.sendall(data.encode())
            
    def host(self,hostFile:str):        
        self.sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HostList[hostFile[0:-3]]=(subprocess.Popen(["python", hostFile]))
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1",2))
            s.listen()
            conn, literal= s.accept()
            conn.sendall(json.dumps(self.port).encode())
            conn.sendall(self.reason.encode())
    def TerminateAll(self):
        for i in self.HostList.keys():
            self.HostList[i].terminate()
if __name__ == "__main__":
    h=Socket("testForPython",22)
    # print("why")
    h.host("echo.py")
    h.host("Udphost.py")
    input()
    h.TerminateAll()
    # s=None
    # while not s:
    #     h.sock.listen()
    #     conn,addr = h.sock.accept()
    #     try:
    #         data = h.recieve(conn)
    #         print("from "+str(addr) + " recieved " +str(data))
    #         s=data
    #     except Exception as e:
    #         print(e)
    # print(s)

    # h.ServerClose()
