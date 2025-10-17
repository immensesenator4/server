import os
from sock import Socket
import socket
import json
import time
s=Socket("testForPython",22)
s.ip=s.getIPs(5,1)[0]
c=Socket("testForPython",22)
f=Socket()
c.sock=f
s.ClientConnect(s.ip,s.port)
s.connect()
s.send(f"n:{json.dumps(s.compressObj(c))}")
s.Disconect()
time.sleep(0.1)
s.connect()
s.send(f"Recieve:n")
m=s.recieve()
s.Disconect()
# print(m)
m=json.loads(m.replace("\\","")[1:-2])
# print(m)

print(s.decompress_obj(m,Socket,{"sock.Socket ":Socket}))

print("propperly dumped json")
print(c.__dict__)