import socket
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
d=client("192.168.12.195",13455 )
d.send("player","with trust i am you to say\n hello new world")
print(f"Received {d.recieve("player")!r}")