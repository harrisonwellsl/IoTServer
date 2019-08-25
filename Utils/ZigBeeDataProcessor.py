from Utils.connectMongo import connect

class DataProcessor(object):
    def __init__(self, dataStr = "",
                 dataBaseHost = 'localhost',
                 dataBasePort = 27017,
                 dataBaseName = 'IotTest',
                 collectionName = 'testCollection'):
        if dataStr == "":
            print("No Data Input....")
            exit(-1)
        self.ID = 'ID'
        self.isUsingBool = 'isUsing'
        self.dataStr = dataStr
        self.dataBaseHost = dataBaseHost
        self.dataBasePort = dataBasePort
        self.dataBaseName = dataBaseName
        self.collectionName = collectionName

    def getCardId(self):
        dataArray = self.dataStr.split(":")
        return dataArray[1]

    def isUsing(self):
        ID = self.getCardId()
        # 这个集合链接的是存储已预约信息的集合
        collection = connect(dataBaseHost = self.dataBaseHost,
                             dataBasePort = self.dataBasePort,
                             dataBaseName = self.dataBaseName,
                             collectionName = 'correctCollection')
        information = collection.find({self.ID : ID})
        if information != None:
            # 需要封装和优化判断是否正在使用的函数          ###2019.06.03
            if information[self.isUsingBool] == True:
                return True
            # 需要封装和优化判断是否正在使用的函数          ###2019.06.03
            elif information[self.isUsingBool] == False:
                return False
            else:
                # 这个异常需要进行处理
                print("Information Error....")
                raise ValueError
        else:
            # 这个异常需要进行处理
            print("Information NotFound....")
            raise ValueError