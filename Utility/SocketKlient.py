import socket
import subprocess


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

    def runVideoM1(self):
        subprocess.call("/home/pi/Documents/exhibition/SHVideo2.py")
        print('runVideoM1')

    def stopVideoM2(self):
        print('stopVideoM2')

    def playVideoM2(self):
        print('playVideoM2')

    def stopVideoM3(self):
        print('stopVideoM3')

    def playVideoM3(self):
        print('playVideoM3')

    def playProjector(self):
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


def takeMessage(message):
    if message == b"run_video":
        t.playVideo()
    elif message == b"stop_video":
        t.stopVideo()
    elif message == b"off_raspberry":
        t.off_raspberry()
    elif message == b"run_projector":
        t.playProjector()
    elif message == b"stop_projector":
        t.stopProjector()
    elif message == b"run_monitor1":
        t.runVideoM1()
    elif message == b"run_monitor2":
        t.playVideoM2()
    elif message == b"run_monitor3":
        t.playVideoM3()
    elif message == b"stop_monitor1":
        t.stopVideoM1()
    elif message == b"stop_monitor2":
        t.stopVideoM2()
    elif message == b"stop_monitor3":
        t.stopVideoM3()
    elif message == b"disconnect":
        t.Disconnect()
    else:
        print("Error: " + message)


if __name__ == '__main__':

    r = True
    sock = socket.socket()
    while r:
        try:
            try:
                print("Повтор подключения")
                sock.connect(('192.168.1.184', 9090))
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
