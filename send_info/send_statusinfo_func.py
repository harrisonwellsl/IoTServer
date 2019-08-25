from Client.connectMongo import connectDB
import time

def send_statusinfo_func(sock, addr, studentNumber):
    print("发送状态信息至客户端{}".format(str(addr)))
    while True:

        try:

            collection = connectDB(Collection = 'correctCollection')
            collection2 = connectDB(Collection = 'studentInformation')

            correct = collection.find_one({'学号':studentNumber})
            student = collection2.find_one({'学号':studentNumber})

            if correct != None and student != None:
                sock.sendall(("这是新加入的状态信息" + str(correct) + str(student)).encode('utf-8'))
                # time.sleep(3)
            time.sleep(3)

        except ConnectionAbortedError as e:
            # print(e.__str__())
            break