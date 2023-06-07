import socket
import pickle
import os

HOST = '127.0.0.1'
PORT = 9090

sock = socket.socket()
sock.connect((HOST, PORT))
p, g, a = 7, 5, 3
A = g ** a % p
sock.send(pickle.dumps((p, g, A))) #отправка чисел


B = pickle.loads(sock.recv(1024))  # полученные данные
K = B ** a % p
key = str(K)

cryptmess = pickle.loads(sock.recv(1024))
print(cryptmess)

decrmess = cryptocode.decrypt(cryptmess, key)
print(decrmess)

sock.close()


