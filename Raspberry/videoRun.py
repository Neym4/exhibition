import os
import subprocess

'''
Модуль для запуска видео из папки
'''
pathVideo = r'/home/pi/Videos'  # Путь до папки с видео
count = 0

list_video = os.listdir(pathVideo)
pid = None

while True:
    try:
        if pid.poll() is None:
            # print("Процесс еще идет")
            pass
        else:
            count = count + 1
            name = list_video[count]
            pid = subprocess.Popen(["omxplayer", os.path.join(pathVideo, name)])
            print("pid=", pid)
            print("pid.poll", pid.poll())
            print("self.pid.pid", pid.pid)
    except AttributeError:
        name = list_video[count]
        pid = subprocess.Popen(["omxplayer", os.path.join(pathVideo, name)])
