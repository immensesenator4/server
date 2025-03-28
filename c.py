import os
from sock import Socket
import socket
s=Socket("testForPython",22)
s.ip = s.getServers()[0]
c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connectServer(s.ip,s.port)
s.send(s.compressObj(s))
s.sock.shutdown(2)
print("sent")