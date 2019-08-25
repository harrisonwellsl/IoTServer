import threading
import socket

def tcpFUNC(sock, addr):
    while True:
        dataArray = []
        while True:
            data = sock.recv(1)
            dataArray.append(data)
            if dataArray[-1].decode('utf-8') == '\n':
                dataArray.pop(-1)
                break
        msgFromClient = b''.join(dataArray).decode('utf-8')
        print(msgFromClient + '---->' + threading.current_thread().getName())

bindThing = ('127.0.0.1', 8888)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(bindThing)
server.listen(100000)
while True:
    sock, addr = server.accept()
    print('A connection built.....')
    t = threading.Thread(target = tcpFUNC, args = (sock, addr))
    t.start()
    print('Active threads ---> ' + str(threading.active_count()))