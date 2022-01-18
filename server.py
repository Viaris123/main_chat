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
        data = user_conn.recv(2048)
        msg = data.decode('utf-8')
        user_adr = user_conn.getpeername()
        print(msg, " from ", user_adr)
        msg_to_send = json.dumps((user_adr, msg)).encode('utf-8')
        send_msg(msg_to_send)


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
