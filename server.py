import socket
import threading
import json


class MessagesDB:
    def __init__(self, sock):
        self.messages = list()
        self.sock = sock
        self.consumer_lock = threading.Lock()
        self.producer_lock = threading.Lock()

    def set_message(self, message):
        self.producer_lock.acquire()
        self.messages.append(message)
        self.producer_lock.release()

    def send_message(self):
        self.consumer_lock.acquire()
        pass


messages = list()


def recv_msg(inputs):
    while True:

        for conn in inputs:
            if conn == sock:
                new_conn, adr = conn.accept()
                inputs.append(new_conn)
            else:
                tmp_msg = conn.recv(2048)
                msg = (tmp_msg.decode('utf-8'))
                messages.append((conn.getpeername(), msg))


def send_msg():
    pass


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8008))
sock.listen(5)
inputs = [sock]
outputs = []


