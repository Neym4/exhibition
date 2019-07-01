import socket
import subprocess
from threading import Thread
import os


# list_VIDEO = os.list_VIDEO(r"C:\Users\admin\Desktop\sdfpidshjfkl")
pathVideo = '/home/pi/Videos'


class KlientRPI():
    def playVideo(self):
        print('run_video')

    def stopVideo(self):
        print('stop_video')

    def sendTheMessage(self):
        print()

    def acceptMessege(self):
        print()

    def stopVideoM1(self):
        print('stop_video')

    def runVideoM1(self, pathVideo):
        # subprocess.call("sh /home/pi/Documents/startVideo.sh %s" % pathVideo)
        subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])
        print('runVideoM1')

    def stopVideoM2(self):

        print('stopVideoM2')

    def playVideoM2(self,pathVideo):
        subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])
        print('playVideoM2')

    def stopVideoM3(self):
        print('stopVideoM3')

    def playVideoM3(self,pathVideo):
        subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])

        print('playVideoM3')

    def playProjector(self,pathVideo):
        subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])

        print('run_projector')

    def stopProjector(self):
        print('stop_projector')


    def SdisconnRpi(self):
        print()

    def conn(self):
        print()

    def Sturnofrscreen(self):
        print()

    def Disconnect(self):
        print('disconnect')

    def off_raspberry(self):
        print("off_raspberry")


t = KlientRPI()



m1 = False
def takeMessage(message, m1, m2, m3, m4):

    if message == b"run_video":
        t.playVideo()
    elif message == b"stop_video":
        t.stopVideo()
    elif message == b"off_raspberry":
        t.off_raspberry()
    elif message == b"run_projector":
        m4 = True
        if m4 == True:
            list = os.listdir(pathVideo)
            for name in list:
                path = os.path.join(pathVideo, name)
                t.playProjector(path)
        else:
            pass
    elif message == b"stop_projector":
        m4 = False
        if m4 == True:
            list = os.listdir(pathVideo)
            for name in list:
                path = os.path.join(pathVideo, name)
                t.playProjector(path)
        else:
            pass
    elif message == b"run_monitor1":
        print("run_monitor1", m1)
        m1 = True
        if m1 == True:
            list = os.listdir(pathVideo)
            for name in list:
                path = os.path.join(pathVideo, name)
                t.runVideoM1(path)
        else:
            pass
    elif message == b"run_monitor2":
        m2 = True
        if m2 == True:
            list = os.listdir(pathVideo)
            for name in list:
                path = os.path.join(pathVideo, name)
                t.runVideoM2(path)
        else:
            pass
    elif message == b"run_monitor3":
        m3 = True
        if m3 == True:
            list = os.listdir(pathVideo)
            for name in list:
                path = os.path.join(pathVideo, name)
                t.runVideoM3(path)
        else:
            pass
    elif message == b"stop_monitor1":
        print("stop_monitor1", m1)
        m1 = False
        if m1 == True:
            list = os.listdir(pathVideo)
            for name in list:
                path = os.path.join(pathVideo, name)
                t.runVideoM1(path)
        else:
            pass
    elif message == b"stop_monitor2":
        m2 = False
        if m2 == True:
            list = os.listdir(pathVideo)
            for name in list:
                path = os.path.join(pathVideo, name)
                t.runVideoM2(path)
        else:
            pass
    elif message == b"stop_monitor3":
        m3 = False
        if m3 == True:
            list = os.listdir(pathVideo)
            for name in list:
                path = os.path.join(pathVideo, name)
                t.runVideoM3(path)
        else:
            pass
    else:
        print("Error: " + message)

variable = Thread(target= takeMessage, args= m1, m2, m3, m4,)

if __name__ == '__main__':

    r = True
    sock = socket.socket()
    while r:
        try:
            try:
                print("Повтор подключения")
                sock.connect(('192.168.1.56', 9090))
                print('try connect')
            except TimeoutError as e:
                sock = socket.socket()
                print("error " + str(e))
            else:
                while True:
                    data = sock.recv(1024)
                    # data.clean()
                    takeMessage(data)
        except BaseException as be:
            sock = socket.socket()
            print("error BE: " + str(be))
        else:
            pass


