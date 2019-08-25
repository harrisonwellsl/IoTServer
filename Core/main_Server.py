from serial_readerThread.serial_reader import Serial_Reader
from serial_sender.serial_sender import Serial_Sender
from Client.ServerThread import ServerThread
from sendTHData.sendTh import sendData

a = Serial_Reader(1, 'Reader')
# b = Serial_Sender(2, 'Sender')
c = ServerThread()
# d = sendData()


a.start()
# b.start()
c.start()
# d.start()

a.join()
# b.join()
c.join()
# d.join()