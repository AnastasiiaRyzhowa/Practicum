import socket
import pickle#преобразования объектов или структур данных в байтовые потоки или строки
import cryptocode

HOST = '127.0.0.1'
PORT = 9090

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

p, g, A = pickle.loads(conn.recv(1024))  # скачали данные 
b = 8
B = g ** b % p
conn.send(pickle.dumps(B))  # отправляем данные обратно

K = A ** b % p
key = str(K)
print('Сообщение:', key)

#применяя ключ шифруем сообщения
cryptmess = cryptocode.encrypt(msg, key)  
conn.send(pickle.dumps(msgEn))
print('Отправленное сообщение:', cryptmess)

conn.close()