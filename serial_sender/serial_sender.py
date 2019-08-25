import threading
from serial_sender.serial_sender_func import serial_sender_func

'''
类继承自threading.Thread类
单独开启一个线程去发送数据到STM32
'''

class Serial_Sender(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        isRunning = True
        print(self.name + '----' + str(self.threadID))
        while isRunning:
            serial_sender_func()