def getMsgFromClient(sock, addr):
    print("Message From Client {}.....".format(str(addr)))
    ch = sock.recv(1024)
    ch = ch.decode('utf-8')
    print(ch)
    return ch