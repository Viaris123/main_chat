import socket
import threading


def send_msg(sock):
    while True:
        msg = input("\n::: Enter message: ")
        if msg == 'x':
            return
        sock.send(msg.encode())

def recv_msg(sock):
    while True:
        msg = sock.recv(1024)
        print("\n")
        print(msg.decode())


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8008))
s = threading.Thread(target=send_msg, args=(client, ))
s.start()
r = threading.Thread(target=recv_msg, args=(client, ))
r.start()
s.join()
r.join()

client.close()