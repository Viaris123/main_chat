import socket
import threading
import json

USERS = []
HOST = '127.0.0.1'
PORT = 8008


def send_msg(msg):
    for user in USERS:
        try:
            user.send(msg)
        except ValueError:
            continue


def msg_pipeline(user_conn):
    print(threading.current_thread().name)
    while True:
        try:
            data = user_conn.recv(2048)
        except ConnectionResetError:
            print(f'User {user_conn} disconnected')
            break

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

        work_thread = threading.Thread(target=msg_pipeline, args=(conn,), daemon=True)
        work_thread.start()
        print(threading.active_count(), "- threads")


server_start()

