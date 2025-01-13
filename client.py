import socket
#type will be stored in the future so we can transmute integers and booleans and lists
# this will happen when client class is made
#what is below is a send and recieve function
#this will continue with a self.host and self. ip adress which i would have to make somethingto search the port i think
HOST =  "192.168.12.195" 
PORT = 13455 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"l=Hello, world")
    data = s.recv(1024)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
    s.connect((HOST, PORT)) 
    s.sendall(b"l= recieve")
    data = s.recv(1024)
    
print(f"Received {data!r}")