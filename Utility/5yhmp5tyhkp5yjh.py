from threading import Thread
import time
m1 = m2 = m3 = m4 = False

def message(message1, tm):
    oldtime = time.time()
    time.sleep = 2
    print (message1)
message("message", 1)
