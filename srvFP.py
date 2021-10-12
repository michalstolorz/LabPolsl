import socket
import sys
from random import randrange

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 server.py <arg1:server ip:this
system IP 192.168.1.6> <arg2:server port:4444 >")
    exit(1)
    
# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = (ip, port)
s.bind(server_address)
s.listen(2)
conn, addr = s.accept()
print("Do Ctrl+c to exit the program !!")
print("####### Server is listening #######")
i = 0
while True:
    data = conn.recv(1024)
    loss = randrange(10000)
    if(loss<1600):
        continue
    conn.sendall(data)
    if (i < 10):
        print("Packet number ", i, " data received: ", data.decode('utf-8'))
    else:
        if i < 100:
            if i % 10 == 0:
            print(i)
    else:
        if i % 100 == 0:
            print(i)
        i += 1


