import socket
import threading
import json

USERS = []
HOST = '127.0.0.1'
PORT = 8008


def send_msg(msg):
    for user in USERS:
        user.send(msg)


def msg_pipeline(user_conn):
    while True:
        msg = user_conn.recv(2048)
        print(msg.decode('utf-8'), " from ", user_conn.getpeername())
        send_msg(msg)


def server_start():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)

    while True:
        conn, adr = sock.accept()
        USERS.append(conn)
        print(f"Connection from {adr}")

        work_thread = threading.Thread(target=msg_pipeline, args=(conn,))
        work_thread.start()


server_start()
