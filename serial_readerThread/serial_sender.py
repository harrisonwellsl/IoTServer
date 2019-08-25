import serial
import time

def serial_sender_open(msg = '', comPort = 'COM3', bod = 115200):
    times = 20
    ser = serial.Serial(comPort, bod)
    while times:
        msgWrite = '#' + msg + '#' + '1' + '#'
        print(msgWrite)
        ser.write(msgWrite.encode("iso-8859-15"))
        time.sleep(0.3)
        times -= 1
    ser.close()

def serial_sender_close(msg='', comPort='COM3', bod=115200):
    times = 20
    ser = serial.Serial(comPort, bod)
    while times:
        msgWrite = '#' + msg + '#' + '0' + '#'
        print(msgWrite)
        ser.write(msgWrite.encode("iso-8859-15"))
        time.sleep(0.3)
        times -= 1
    ser.close()

if __name__ == "__main__":
    #serial_sender_open('2')
    # # time.sleep(5)
    serial_sender_close('1')