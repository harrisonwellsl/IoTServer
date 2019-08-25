import threading
import socket
import time
from Client.forEveryThread import forEveryThread
from Client.send_temp_fuc import send_temp

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        bindThings = ("0.0.0.0", 8888)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(bindThings)
        server.listen(100000)
        print("Server Started.....")
        while True:
            sock, addr = server.accept()
            print("A Client Connected....")
            sendmsg = threading.Thread(target = send_temp, args = (sock, addr))
            t = forEveryThread(sock = sock, addr = addr)
            t.start()
            # time.sleep(1)
            sendmsg.start()