from threading import Thread
import time
m1 = m2 = m3 = m4 = False

def message(message1, tm):
    oldtime = time.time()
    while True:
        if time.time() - oldtime >= tm:
            oldtime = time.time()
            print (message1, str(oldtime))

t1 = Thread(target = message, args = ("message", 1, ))
t2 = Thread(target = message, args = ("hello", 2, ))
t3 = Thread(target = message, args = ("good", 3, ))
#
# t1.start()
# t2.start()
# t3.start()

class class_T1:
    def __init__(self):
        print("init t1")

    def printf(self, message):
        print("t1", message)

class class_T2(class_T1):

    def __init__(self):
        print("class t2")

    def printf2(self, message):
        print("t2", message)

obj1 = class_T2()
obj1.printf("bhhhh")

b = 2
def t():
    eee = 0
    if 'eee' in locals():
        print("ok")
    if 'eee' in globals():
        print("ok1")

if __name__ == '__main__':
    a = 1
    t()
    print(locals())
    print(globals())