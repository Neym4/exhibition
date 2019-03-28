import socket
#import vlc
sock = socket.socket()
sock.connect(('192.168.1.184', 9090))
print('connect')
data = sock.recv(1024)
print(data)
sock.send(b"Hello Daniel!")

if data == b'run_video':
    print('runvideo')



# print(data)

class KlientRPI ():

    def sendTheMessage (self):
        print()


    def acceptMessege(self):
        print()

    def stop(self):
        #pygame.mixer.music.pause();
        global set
        set = 0  # set =0 ,means song is  not playing currently

    def playVideo (self):
         #comm =  "/home/aayushshivam7/python\ projects/pygam_vlc.py "
         #call(["python","pygam_vlc.py","abc.mp4"])
        #global player
        #player = vlc.MediaPlayer(r"C:\Users\admin\Desktop\sdfpidshjfkl\МЫ.mp4")
        #player.play()
        print('Print video')

    def StVid(self,event):

        global file
        player.stop()
        file = ""
    print()

    def SdisconnRpi(self):
        print()

    def conn(self):
        print()

    def Sturnofrscreen (self):
        print()

#t = KlientRPI()
#t.playVideo('jj')
# sock.close()