import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bindThing = ('127.0.0.1', 8888)
server.bind(bindThing)
server.listen(10)
sock, addr = server.accept()
while True:
    dataArray = []
    while True:
        data = sock.recv(1)
        dataArray.append(data)
        if dataArray[-1].decode('utf-8') == '\n':
            dataArray.pop(-1)
            break
    msgFromClient = b''.join(dataArray).decode('utf-8')
    if msgFromClient.lower() == 'exit':
        break
    print(msgFromClient)
server.close()