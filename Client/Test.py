# -*- coding: utf-8 -*-
import socket

bindThings = ("192.168.43.61", 8888)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(bindThings)
client.sendall("post:A101:seat1:time1:12345".encode("utf-8"))
client.close()