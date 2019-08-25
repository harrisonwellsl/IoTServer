from serial_readerThread.serial_reader import Serial_Reader

t = Serial_Reader(1, "serial_readerThread")
t.start()
t.join()