from omxplayer import OMXPlayer
from time import sleep

playerA = OMXPlayer('path/to/a.mp4', args=['-b', '--loop'])
playerB = OMXPlayer('path/to/b.mp4', args=['-b'])
playerC = OMXPlayer('path/to/c.mp4', args=['-b'])

playerA.play()

while True:
    if Button1PressedFlag==True: #set in interrupt
        Button1PressedFlag=False
        playerA.pause()
        playerB.play()
        while playerB.is_playing():
            sleep(0.2)
        playerB.quit()
        playerA.play()
    if Button2PressedFlag==True: #set in interrupt
        Button2PressedFlag=False
        playerA.pause()
        playerC.play()
        while playerC.is_playing():
            sleep(0.2)
        playerC.quit()
        playerA.play()