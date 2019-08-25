from Client.connectMongo import connectDB

def requestResponse(sock, addr):
    print("Send Usable Message to {}....".format(str(addr)))
    #这里连接的是可用信息数据库
    collection = connectDB(Collection = "usableClassroom")
    documents = collection.find()
    List = []
    for document in documents:
        document.pop('_id')
        className = document.pop('className')
        for eachSeat in document.keys():
            seat = document[eachSeat]
            # print(eachSeat)
            for eachTime in seat.keys():
                time = seat[eachTime]
                # print(eachTime)
                if time['是否被占用'] == False:
                    List.append((className + ':' + eachSeat + ':' + eachTime + '\n').encode('utf-8'))
    sock.sendall(b''.join(List))