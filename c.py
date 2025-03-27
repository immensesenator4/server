import os
from host import Socket
import socket
s=Socket("test",22)
s.ip = s.getServers()[0]
c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((s.ip,s.port))
c.sendall("hi".encode())
print("sent")