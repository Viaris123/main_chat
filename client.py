import socket
import threading
import json


def incom_msg():
    while True:
        data = sock.recv(2048)
        msg_tuple = json.loads(data, encoding='utf-8')
        msg_text = msg_tuple[1]
        msg_adr = msg_tuple[0]
        print(msg_text, ' from ', msg_adr)


def client_pipeline():
    while True:
        thread1 = threading.Thread(target=incom_msg, daemon=True)
        thread1.start()

        sock.send(input("Enter message: ").encode('utf-8'))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8008))

client_pipeline()
