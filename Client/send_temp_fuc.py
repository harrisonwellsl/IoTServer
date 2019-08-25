from Client.connectMongo import connectDB
import time

def send_temp(sock, addr):
    print("Send temp data to {}".format(str(addr)))
    collection = connectDB(Collection = 'th')
    # collection2 = connectDB(Collection = 'correctCollection')
    # collection3 = connectDB(Collection = 'studentInformation')
    # info = str(collection2.find_one({'学号':msg})) + str(collection3.find_one({'学号':msg}))
    while True:
        for each in collection.find():
            # if info:
            #     sock.sendall(info.encode('utf-8'))
            try:
                sock.sendall(("TH:" + each['T'] + ':' + each['H']).encode('utf-8'))
            except (ConnectionResetError, ConnectionAbortedError) as e:
                print(str(e))
                break
            time.sleep(5)
        break
