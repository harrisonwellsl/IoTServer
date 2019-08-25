import pymongo

'''
连接数据库，可更改默认数据库地址和数据库集合名称
'''
def connectDB(Host = "localhost", Port = 27017, DB ="IotTest", Collection ="testCollection"):
    client = pymongo.MongoClient(Host, Port)
    db = client[DB]
    collection = db[Collection]
    return collection