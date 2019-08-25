import socket
import threading

def test():
    bindThing = ('127.0.0.1', 8888)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(bindThing)
    while True:
        msg = input("输入消息：")
        client.sendall((msg + '\n').encode('utf-8'))
    client.close()

thread = []
for i in range(0, 100000):
    t = threading.Thread(target = test)
    thread.append(t)

for t in thread:
    t.start()

for t in thread:
    t.join()