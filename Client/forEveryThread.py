import threading
from Client.returnMsg import returnMsg
from Client.connectMongo import connectDB
from Client.getMsgFromClient import getMsgFromClient
from Client.send_temp_fuc import send_temp
from send_info.send_statusinfo_func import send_statusinfo_func
from serial_readerThread.serial_sender import serial_sender_open, serial_sender_close
from Client.requestResponse import requestResponse

class forEveryThread(threading.Thread):
    def __init__(self, sock, addr):
        threading.Thread.__init__(self)
        self.sock = sock
        self.addr = addr

    def run(self):
        passIt = False
        collection = connectDB(Collection = "studentInformation")
        collection2 = connectDB(Collection = "correctCollection")
        msg = getMsgFromClient(sock = self.sock, addr = self.addr)
        if msg.find("login") == 0:
            studentNumber = msg.split(':')[1]
            print(studentNumber)
            studentPassword = msg.split(':')[2]
            print(studentPassword)
            information = collection.find_one({'学号':studentNumber})
            print(information)

            send_status = threading.Thread(target = send_statusinfo_func, args = (self.sock, self.addr, studentNumber))
            # send_status.start()

            if information != None and information['密码'] == studentPassword :
                correctInformation = collection2.find_one({'学号':studentNumber})

                # sendmsg = threading.Thread(target=send_temp, args=(self.sock, self.addr, studentNumber))
                # sendmsg.start()

                if correctInformation != None and correctInformation['签到情况'] == "未签退":
                    self.sock.sendall("Operate Successfully".encode('utf-8'))
                    correctInformation.pop("_id")
                    information.pop("_id")
                    self.sock.sendall((str(correctInformation) + str(information)).encode('utf-8'))
                    requestResponse(sock=self.sock, addr=self.addr)
                    # self.sock.sendall("请先关闭实验室开关！".encode('utf-8'))
                    msg2 = getMsgFromClient(sock = self.sock, addr = self.addr)
                    print(msg2)
                    if msg2 == "close":
                        serial_sender_close(msg = correctInformation['座位'][-1])

                elif correctInformation != None and correctInformation['isUsing'] == False and correctInformation['签到情况'] == "已预约":
                    self.sock.sendall("Operate Successfully".encode('utf-8'))
                    correctInformation.pop("_id")
                    information.pop("_id")
                    self.sock.sendall((str(correctInformation) + str(information)).encode('utf-8'))
                    requestResponse(sock = self.sock, addr = self.addr)
                    # self.sock.sendall("已预约，现在可选择打开实验室供电开关！".encode('utf-8'))
                    msg3 = getMsgFromClient(sock=self.sock, addr=self.addr)
                    print(msg3)
                    if msg3 == "open":
                        serial_sender_open(msg = correctInformation['座位'][-1])
                    else:
                        self.sock.sendall("请先完成已预约实验。".encode('utf-8'))

                elif correctInformation == None or correctInformation['签到情况'] == "已签退":
                    passIt = True
                    self.sock.sendall("Operate Successfully".encode('utf-8'))
                    # self.sock.sendall((information['名字'] + information['院系'] + information['班级'] + information['角色']).encode('utf-8'))
                    if correctInformation != None:
                        correctInformation.pop("_id")
                        information.pop("_id")
                        self.sock.sendall((str(correctInformation) + str(information)).encode('utf-8'))
                    elif correctInformation == None:
                        information.pop("_id")
                        self.sock.sendall(('“签到情况“”:“未预约”' + str(information)).encode('utf-8'))

                    send_status.start()
        while passIt:
            returnMsg(sock = self.sock, addr = self.addr, studentNumber = studentNumber)
        self.sock.sendall("Operate failed".encode('utf-8'))
        exit(-1)