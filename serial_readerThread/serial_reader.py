import threading
import serial
from serial_readerThread.solveStrFromSerial import solveStrFromSerialID
from serial_readerThread.solveStrFromSerial import solveStrFromSerialTH
from serial_readerThread.serial_reader_func import serial_reader_func
import time

'''
此类继承自threading.Thread类
用于在服务器上单独开启一个线程将在串口读取的数据进行分析
'''

class Serial_Reader(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        isRunning = True
        print(self.name + '----' + str(self.threadID) + "-----串口接收线程打开.....")
        while(isRunning):
            try:
                serialData = serial_reader_func()
                if serialData.find('Coord') == 0:
                    print(serialData)
                    time.sleep(0.3)
                    solveStrFromSerialID(serialData)
                elif serialData.find('T&H') == 0:
                    print(serialData)
                    solveStrFromSerialTH(serialData)
                else:
                    print("Data Error")
                    raise ValueError
            except (ValueError, serial.serialutil.SerialException, UnboundLocalError) as e:
                print(e.__str__())
                continue