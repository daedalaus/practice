import socket

server = socket.socket()
server.bind(('127.0.0.1',8000))
server.listen(3)
conn, addr = server.accept()
data = True
while data:
    data = conn.recv(1024)
    # msg = input()
    # if msq=="any code you mean to exit": break
    conn.sendall(data)
    print(data)
conn.close()
server.close()
