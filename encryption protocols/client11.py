import socket
import pickle
import cryptocode
HOST = '127.0.0.1'
PORT = 8080
sock = socket.socket()
sock.connect((HOST, PORT))
p, g, a = 56, 23, 9
A = g ** a % p
sock.send(pickle.dumps((p, g, A)))  #отправка чисел серверу
B = pickle.loads(sock.recv(1024))  # полученные данные
K = B ** a % p
key = str(K)
cipherword = pickle.loads(sock.recv(1024))
print('Шифруем сообщение:', cipherword)
word = cryptocode.decrypt(cipherword, key)
print('Расшифровываем сообщение:', word)

sock.close()
