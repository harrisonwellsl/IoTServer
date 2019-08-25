from Client.getMsgFromClient import getMsgFromClient
from Client.requestResponse import requestResponse
from Client.postResponse import postResponse
from serial_readerThread.serial_sender import serial_sender_close
from Client.connectMongo import connectDB


def returnMsg(sock, addr, studentNumber = 'studentNumber'):
    print("现在开始正常收发消息")
    print("查询可用信息")
    requestResponse(sock=sock, addr=addr)
    msg = getMsgFromClient(sock = sock, addr = addr)
    if msg == '':
        print("关闭当前链接")
        exit(-1)
    else:
        if msg == "close":
            collection = connectDB(Collection = 'correctCollection')
            information = collection.find_one({'学号':studentNumber})
            serial_sender_close(msg=information['座位'][-1])
        print("确认预约信息")
        postResponse(sock = sock, addr = addr, msg = msg[5:])