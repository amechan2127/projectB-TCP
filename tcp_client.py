import socket
from datetime import datetime
from struct import *
import time

start = time.time()

address = ('192.168.11.2', 10000)
max_size = 4096
size=500

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
f=open('./pyramid.jpg', 'rb') 
data = f.read()
f.close()

end=int(len(data)/size)+1
all_data=len(data)
l=pack('H',end)
client.send(l)
a=client.recv(max_size)
print(all_data)
print(size)

for d in range(end):
	raw=data[d*size:(d+1)*size]
	client.send(raw)
	r=client.recv(max_size)
	print(unpack('H',r))

print('finish')
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
client.close()

elapsed_time= time.time() -start
print("elapsed_time:{0}".format(elapsed_time)+"{sec}")