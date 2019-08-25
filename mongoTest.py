from Utils.connectMongo import connect
from serial_readerThread.serial_reader_func import serial_reader_func

collection = connect(dataBaseName = '黄健', collectionName = '最帅')
# data = serial_reader_func()
insert_data = {'温度':32}

# data = {'名字':'黄健', '卡号':250}
collection.insert_one(insert_data)
collection