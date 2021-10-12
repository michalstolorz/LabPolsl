import random
import socket
import sys
import time
import select

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
    exit(1)
random.seed()

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server_address = (ip, port)
s.connect(server_address)
s.setblocking(0)
print("Do Ctrl+c to exit the program !!")
tmstart=time.time()
lost=0
for i in range(1, 2000):
    #store current time
    t1=str(time.time());
    s.sendall(t1.encode('utf-8'))
    ready = select.select([s], [], [], 5)if ready[0]:
    if ready[0]:
        data = s.recv(4096)
        diff=time.time()-float(data.decode('utf-8'))
        print("Response time {:.9f}".format(diff))
    else:
        lost+=1
        print("Packet lost {:d}".format(lost))
    rnd=abs(random.gauss(0.01,0.033)) # 36+/- per second
    time.sleep(rnd)
s.close()

