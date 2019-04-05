import socket


#import vlc
import subprocess


# sock = socket.socket()
# sock.connect(('192.168.1.184', 9090))
# print('connect')
# data = sock.recv(1024)
# print(data)
# sock.send(b"Hello Daniel!")
# print("Hello Daniel!")


# print(data)

class KlientRPI():

    def sendTheMessage(self):
        print()

    def acceptMessege(self):
        print()

    def stopVideo(self):
        # pygame.mixer.music.pause();
        # global set
        # set = 0  # set =0 ,means song is  not playing currently
        print('stop_video')

    def playVideo(self):
        # comm =  "/home/aayushshivam7/python\ projects/pygam_vlc.py "
        # call(["python","pygam_vlc.py","abc.mp4"])
        # global player
        #player = vlc.MediaPlayer(r"C:\Users\admin\Desktop\sdfpidshjfkl\we.mp4")
        #player.play()
        #subprocess.call(r"C:\Users\admin\Desktop\sdfpidshjfkl\we.mp4", shell=True)
        print('Play video')

    # def StVid(self,event):
    #
    #     global file
    #     player.stop()
    #     file = ""
    # print()

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

t.playVideo()

def takeMessage(message):
    if message == b'run_video':
        t.playVideo()
    elif message == b'stop_video':
        t.stopVideo()
    elif message == b'off_raspberry':
        t.off_raspberry()
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
                    takeMessage(data)
        except BaseException as be:
            sock = socket.socket()
            print("error BE: " + str(be))
        else:
            pass


