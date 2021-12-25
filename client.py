import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.198.0.0', 1234))
client.sendall(b'Hello Internet')

data = client.recv(1024)
print(data.decode())
client.close()