import socket
import threading
import json
import sqlite3

USERS = {}
HOST = '127.0.0.1'
PORT = 8008

connect = sqlite3.connect('app_db.db', check_same_thread=False)


def send_msg(msg):
    users = USERS.keys()
    for user in users:
        try:
            user.send(msg)
        except ValueError:
            continue


def msg_pipeline(user_conn):

    while True:
        try:
            data = user_conn.recv(2048)
        except ConnectionResetError:
            print(f'User {user_conn} disconnected')
            USERS.pop(user_conn)
            break

        msg = data.decode('utf-8')
        user_adr = user_conn.getpeername()
        print(msg, " from ", user_adr)
        msg_to_send = json.dumps((USERS.get(user_conn), msg)).encode('utf-8')
        send_msg(msg_to_send)


def server_start():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)

    while True:
        conn, adr = sock.accept()
        try:
            username = conn.recv(1024)
        except ConnectionResetError:
            print('Ooops... Client not connected!')
            continue
        USERS[conn] = username.decode('utf8')
        print(f"Connection from {adr}")
        print(USERS)

        work_thread = threading.Thread(target=msg_pipeline, args=(conn,), daemon=True)
        work_thread.start()


server_start()

