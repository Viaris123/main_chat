import socket
import threading
import os
import json


class Messages:

    def __init__(self):
        self.messages = list()
        self.consumer_lock = threading.Lock()
        self.producer_lock = threading.Lock()

    def set_message(self, message):
        self.producer_lock.acquire()
        self.messages.append(message)
        self.producer_lock.release()

    def print_messages(self):
        self.consumer_lock.acquire()
        # os.system('cls')
        for msg in self.messages:
            print(f"From: {msg[0]} ::: {msg[1]}")
        self.consumer_lock.release()


class ShowMsgHistory(threading.Thread):

    def __init__(self, messages):
        threading.Thread.__init__(self)
        self.msg_list_len = 0
        self.messages = messages

    def run(self):
        self.print_msg_history()

    def print_msg_history(self):
        while True:
            if self.msg_list_len <= len(self.messages.messages):
                self.messages.print_messages()
                self.msg_list_len +=1
            else:
                continue


class IncomMsg(threading.Thread):

    def __init__(self, sock, messages):
        threading.Thread.__init__(self)
        self.sock = sock
        self.messages = messages

    def run(self):
        self.recv_msg()

    def recv_msg(self):
        while True:
            incom_msg = self.sock.recv(2048)
            msg = json.loads(incom_msg)
            self.messages.set_message(msg)


class SendMsg(threading.Thread):

    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        self.send_msg()

    def send_msg(self):
        while True:

            msg = input("Type some text: ")
            self.sock.send(msg.encode('utf-8'))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8008))
    messages = Messages()
    thread1 = ShowMsgHistory(messages)
    thread2 = IncomMsg(sock, messages)
    thread3 = SendMsg(sock)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    sock.close()


main()
