import socket
import pickle#преобразования объектов или структур данных в байтовые потоки или строки
import cryptocode

HOST = '127.0.0.1'
PORT = 8080
sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
p, g, A = pickle.loads(conn.recv(1024))  # скачали данные
b = 9
B = g ** b % p
conn.send(pickle.dumps(B))  # отправляем данные обратно клиенту
K = A ** b % p
key = str(K)
word = 'Hello word'
print('Сообщение:', word, key)
#применяя ключ шифруем сообщения
cipherword = cryptocode.encrypt(word, key)
conn.send(pickle.dumps(cipherword))
print('Отправленное сообщение:', cipherword)

conn.close()
