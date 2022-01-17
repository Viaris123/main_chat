import socket
import threading
import json


def incom_msg():
    while True:
        msg= sock.recv(2048)
        print(msg.decode('utf-8'))


def client_pipeline():
    while True:
        thread1 = threading.Thread(target=incom_msg, daemon=True)
        thread1.start()

        sock.send(input("Enter message: ").encode('utf-8'))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8008))

client_pipeline()
