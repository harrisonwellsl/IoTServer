import threading
import time

class test(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        for i in range(0, 5):
            print(str(self.threadID) + "---" + self.name + "---" + str(time.time()))
            # time.sleep(1)

thread = []
for i in range(0, 1000):
    thread.append(test(i, "Thread - " + str(i)))

start = time.time()
for t in thread:
    t.start()

for t in thread:
    t.join()

end = time.time()

print(end - start)