from datetime import datetime
import socket
from struct import *
#from time import sleep
address = ('192.168.11.2', 10000)
max_size = 1024*5
import os
if os.path.isfile('text.jpg'):
    os.remove('text.jpg')
print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)
 
client, addr = server.accept()
 
num = client.recv(max_size)
client.send(num)
 
allsize=unpack('H',num)
print(allsize)
 
 
#num1 = client.recv(max_size)
#client.send(num1)
 
#size=unpack('H',num1) 
#print(size)
 
 
#while data[-6:-1] != b'finish':
#for i in range(n[0]+2):
f = open('text.jpg', 'ab') # 書き込みモードで開く
#for i in range(0,allsize[0],size[0]):
for i in range(allsize[0]):
    data = client.recv(max_size)
    #data_receive.append(data)
    j = pack('H',i)
    print(i)
    f.write(data) # 引数の文字列をファイルに書き込む
    client.send(j)
 
#print('At', datetime.now(), client, 'said',data)   
 
f.close() # ファイルを閉じる
client.sendall(b"Finish")
client.close()
server.close()