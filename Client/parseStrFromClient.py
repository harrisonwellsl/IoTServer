def parseStrFromClient(msg = ""):
    if msg.find("request") == 0:
        return True
    elif msg.find("post") == 0:
        return False
    else:
        print("Client Information Error...")
        raise ValueError