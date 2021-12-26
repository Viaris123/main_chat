import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.198.0.0', 1234))
serv.listen(1)
print(":::Sever is listening...")
con, adr = serv.accept()
print(f"Connection from: {adr[0]}")
while True:
    data = con.recv(1024)
    con.sendall(data)
con.close()
