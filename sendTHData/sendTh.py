from Client.connectMongo import connectDB
import socket
import threading

class sendData(threading.Thread):
    def __init__(self, sock, addr, msg = ''):
        super.__init__(self)

    def run(self):
        print("开始发送温度以及湿度数据.....")
        collection = connectDB(Collection="th")
        collection2 = connectDB(Collection = 'correctCollection')
        collection3 = connectDB(Collection = 'studentInformation')
        bind_thing = ("0.0.0.0", 9999)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(bind_thing)
        server.listen(10)
        sock, addr = server.accept()
        while True:
            print("显示器端已建立连接.....")
            for each in collection.find():
                if each:
                    try:
                        sock.sendall("TH:" + each['T'] + ':' + each['H'])
                    except ConnectionResetError as e:
                        print(str(e))
                        break