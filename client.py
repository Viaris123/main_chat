import socket


def get_message():
    msg = input("::: Enter message: ")
    return msg.encode()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.198.0.0', 1234))
while True:
    state = input("Press 'x' to exit. Press any key to continue.")
    if state == 'x':
        break
    outMsg = input("::: Enter message: ")
    client.sendall(outMsg.encode())
    inMsg = client.recv(1024)
    print(inMsg.decode())

client.close()