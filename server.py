import socket
import threading
import json


class MessagesDB:
    def __init__(self):
        self.messages = list()
        self.consumer_lock = threading.Lock()
        self.producer_lock = threading.Lock()

    def set_message(self, message):
        self.producer_lock.acquire()
        self.messages.append(message)
        self.producer_lock.release()

    def get_message(self):
        self.consumer_lock.acquire()
        message = self.messages[-1]
        self.consumer_lock.release()
        return message


def recv_msg(inputs, outputs, messages):
    while True:

        for conn in inputs:
            if conn == sock:
                new_conn, adr = conn.accept()
                inputs.append(new_conn)
            else:
                tmp_msg = conn.recv(2048)
                msg = (tmp_msg.decode('utf-8'))
                messages.set_message((conn.getpeername(), msg))
                outputs.append(conn)


def send_msg(outputs, messages):
    while True:
        for conn in outputs:
            print(messages.get_message())  # for debug only
            conn.send(json.dumps(messages.get_message()).encode('utf-8'))
            outputs.remove(conn)



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8008))
sock.listen(5)
inputs = [sock]
outputs = []
messages = MessagesDB()
thread1 = threading.Thread(target=recv_msg, args=(inputs, outputs, messages, ))
thread2 = threading.Thread(target=send_msg, args=(outputs, messages, ))
thread1.start()
thread2.start()

thread1.join()
thread2.join()

