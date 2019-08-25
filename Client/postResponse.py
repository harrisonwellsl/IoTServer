from Client.connectMongo import connectDB
from serial_readerThread.serial_sender import serial_sender_close

def postResponse(sock, addr, msg = ''):
    print("Post Information From {}".format(str(addr)))
    print(msg)
    requestInformation = msg.split(':')
    # 这里连接的是可用教室信息
    collection = connectDB(Collection = 'usableClassroom')
    collection2 = connectDB(Collection = 'correctCollection')
    collection3 = connectDB(Collection = 'studentInformation')
    studentInformaton = collection3.find_one({'学号':requestInformation[3]})
    information = collection2.find_one({'学号':requestInformation[3]})

    if information == None or information['签到情况'] == '已签退':
        document = collection.find_one({'className':requestInformation[0]})
        document[requestInformation[1]][requestInformation[2]]['是否被占用'] = True
        document[requestInformation[1]][requestInformation[2]]['使用人员'] = requestInformation[3]
        # updateInformation = {"$set":{requestInformation[1]:{requestInformation[2]:{'是否被占用':True}}}}

        # info = collection.find_one({'className': requestInformation[0]})
        # print(info)

        collection.update({'className':requestInformation[0]}, document)
        findStudentInformation = connectDB(Collection = 'studentInformation')
        IDInformation = (findStudentInformation.find_one({'学号':requestInformation[3]}))['ID']
        nameInformation = (findStudentInformation.find_one({'学号': requestInformation[3]}))['名字']
        correctInformation = {'教室':requestInformation[0], '座位':requestInformation[1], '时间':requestInformation[2], '名字':nameInformation, '学号':requestInformation[3], 'ID':IDInformation, 'isUsing':False, '签到情况':'已预约'}
        # 这里连接到预约数据库用于插入预约信息
        collection2 = connectDB(Collection = 'correctCollection')
        collection2.insert_one(correctInformation)
        sock.sendall(('Successful' + str(correctInformation) + str(studentInformaton)).encode('utf-8'))
    else:
        sock.sendall(('请先完成预约实验' + str(information)).encode('utf-8'))