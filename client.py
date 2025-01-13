import socket

HOST =  "192.168.12.195" # The server's hostname or IP address
PORT = 13455  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"l=Hello, world")
    data = s.recv(1024)
print(f" {data!r}")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   
    s.connect((HOST, PORT)) 
    s.sendall(b"l= recieve")
    data = s.recv(1024)
    

print(f"Received {data!r}")