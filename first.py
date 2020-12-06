import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 7777))
sock.listen(1)
stream, address = sock.accept()
data = stream.recv(1024)
sock.setblocking(True)
print(data.decode('utf-8'))
stream.send('hello client'.encode('utf-8'))
sock.close()