import socket
import select
from queue import Queue

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(False)
sock.bind(('127.198.0.0', 1234))
sock.listen(5)
inputs = [sock]
outputs = []
messages = {}
print(":::Sever is listening...:::")

while True:
    read_list, send_list, ex_list = select.select(inputs, outputs, inputs)

    for conn in read_list:

        if conn == sock:
            new_client, client_addr = conn.accept()
            print(f':::Connection from {client_addr} successful:::')
            new_client.setblocking(False)
            inputs.append(new_client)
        else:
            incom_msg = conn.recv(1024)
            if incom_msg:
                messages[conn] = incom_msg
                if conn not in outputs:
                    outputs.append(conn)
            else:
                print(f':::Client {conn} disconnected:::')
                inputs.remove(conn)
                if conn in outputs:
                    outputs.remove(conn)

                conn.close()
                del messages[conn]

    for conn in send_list:
        msg = messages.get(conn, None)

        if len(msg):
            conn.send(msg)
        else:
            outputs.remove(conn)

    for conn in ex_list:
        print(f':::Client {conn} suddenly disconnected:::')
        if conn in inputs:
            inputs.remove(conn)
        if conn in outputs:
            outputs.remove(conn)
        conn.close()
        del messages[conn]