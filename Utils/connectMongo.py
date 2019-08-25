import pymongo

'''
链接MongoDB的函数
默认链接主机localhost(127.0.0.1)，以及端口号27017，默认数据库为Test，默认集合为testCollection
可以根据需要传递参数更改
dataBaseHost，dataBasePort，dataBaseName，collectionName
依次更改的参数代表的是
主机名，数据库端口号，数据库抿成，集合名称
返回的是集合对象
'''

def connect(dataBaseHost = 'localhost', dataBasePort = 27017, dataBaseName = 'Test', collectionName = 'testCollection'):
    MongoClient = pymongo.MongoClient(dataBaseHost, dataBasePort)
    db = MongoClient[dataBaseName]
    collection = db[collectionName]
    return collection