import os
from sock import Socket
import socket
s=Socket("testForPython",22)
s.ip = s.getServers()[0]
c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connectServer(s.ip,s.port)
m=s.Echo("n","nooooooo",False)

print(m)