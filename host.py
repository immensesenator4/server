import socket
class Host(object):
    def __init__(self,size:int,port:int):
            self.port=port
            self.s = socket.socket()
            self.hostname = socket.gethostname()
            self.ip_address = socket.gethostbyname(self.hostname)
            print(self.ip_address)
            
            self.data={}
            self.var=[]
    def get_person(self):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.ip_address, self.port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        if ("recieve" in f"{data!r}" ):
                            l=""
                            print(True)
                            count=0
                            for i in f"{data!r}":
                                if count==0:
                                     pass
                                elif i == "=":
                                     break
                                else:
                                     l+=i
                                count+=1
                            print("l")
                            
                                 
                            if l in self.var:
                                self.send(self.data[l],conn)
                            else:
                                 self.send(b'N/a',conn)
                        else:
                            l=""
                            count=0
                            for i in f"{data!r}":
                                if count==0:
                                     pass
                                elif i == "=":
                                     break
                                else:
                                     l+=i
                                count+=1
                            self.var.append(l)
                            print(l)
                            count = len(l)+1
                            new_data=""
                            for char in f"{data!r}":
                                 if count<0:
                                      new_data+=char
                                 count-=1
                            self.data[l]= new_data.encode()
                            self.send(b'recieved',conn)
                        return data,addr
    def send(self,data:bytes,conn):
        conn.sendall(data)

h=Host(2,13455)
h.get_person()
h.get_person()