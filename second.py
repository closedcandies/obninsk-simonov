import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9090))
sock.connect(('', 7777))
sock.send('hello server'.encode('utf-8'))
data, server = sock.recvfrom(1024)
print(data.decode('utf-8'))
