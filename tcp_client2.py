import socket
from datetime import datetime

address = ('192.168.70.152', 10000)
max_size = 5000

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
with open('./pyramid.jpg', 'rb') as f:
    data = f.read()

client.sendall(data)
print('finish')
client.send(b'finish')
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
client.close()
