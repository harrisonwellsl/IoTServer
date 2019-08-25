import serial
import time
from Utils.connectMongo import connect

'''
服务器的一个串口链接在STM32上，STM32用于链接显示器显示当前使用者信息
此函数用于读取发送数据
默认发送的是串口COM3，波特率115200，超时时间设置为0.5
如果需要，可以更改comPort，bod，timeout参数
依次更改的参数为
发送的串口，波特率，超时参数
'''

def serial_sender_func(comPort = 'COM5', bod = 115200, timeout = 0.5):
    isRunning = True
    ser = serial.Serial(comPort, bod, timeout)
    collection = connect()
    while isRunning:
        for each in collection.find():
            if each['isUsing'] == True:
                sendData = each['ID'] + ':' + each['学号'] + ':' + each['姓名']
                ser.write(sendData.encode('iso-8859-15'))
                time.sleep(3)
            else:
                pass