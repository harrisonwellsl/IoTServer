import serial

'''
ZigBee的PAN网络协调器连接在服务器的一个串口上
此函数用于读取串口数据
默认读取的是串口COM3，波特率115200，超时时间设置为0.5
如果需要，可以更改comPort，bod，timeout参数
依次更改的参数为
读取的串口，波特率，超时参数
'''

def serial_reader_func(comPort = 'COM3', bod = 115200):
    strList = []
    try:
        ser = serial.Serial(comPort, bod)
        while True:
            ch = ser.read()
            str = ch.decode("iso-8859-15")
            if str != '\n':
                strList.append(str)
            else:
                break
            pass
        return ''.join(strList)
        # 返回值为从串口读取到的字符串数据
    except serial.serialutil.SerialException as e:
        print(str(e))
        # continue