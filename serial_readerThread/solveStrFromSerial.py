from Client.connectMongo import connectDB
from serial_readerThread.serial_sender import serial_sender_close, serial_sender_open
import time

def solveStrFromSerialID(msg = ''):
    collection = connectDB(Collection = "correctCollection")
    collection2 = connectDB(Collection = "usableClassroom")
    information = msg.split(':')
    print(information)
    find = collection.find_one({'ID':information[1]})
    print(find)
    if find != None:
        if find['签到情况'] == '已预约':
            find['isUsing'] == True
            find['签到情况'] = '未签退'
            collection.update({'ID':information[1]}, find)
            serial_sender_open(find['座位'][-1])
            time.sleep(2)
        elif find['签到情况'] == '未签退':
            find['isUsing'] == False
            find['签到情况'] = '已签退'
            collection.update({'ID': information[1]}, find)
            # collection.find_one_and_delete({'ID': information[1]})
            classFind = collection2.find_one({"className": find['教室']})
            classFind[find['座位']][find['时间']]['是否被占用'] = False
            classFind[find['座位']][find['时间']]['使用人员'] = ""
            collection2.update({"className": find['教室']}, classFind)
            serial_sender_close(find['座位'][-1])
            time.sleep(2)
        else:
            print("Information Error.....1")
            time.sleep(2)
            raise ValueError
    else:
        print("Information Error.....2")
        time.sleep(2)
        raise ValueError

def solveStrFromSerialTH(msg = ''):
    collection = connectDB(Collection = "th")
    information = msg.split(':')
    TH = information[1].split(' ')
    T = TH[0]
    H = TH[1]
    if T.strip() != "00" and H.strip() != "00":
        print(T, H)
        collection.insert_one({'T':T, 'H':H})
    time.sleep(1)
    # ser = serial.Serial(comPort = 'COM3', bod = 115200, timeout = 0.5)
    # ser.write(T.encode('iso-8859-15'))
    # ser.write(H.encode('iso-8859-15'))