import socket
import subprocess
from threading import Thread, Event
import os
import signal
import time


pathVideo = r'/home/pi/Videos'  # Путь до папки с видео


class KlientRPI:

    def getListVideo(self):
        global pathVideo
        self.count = 0

        self.list_video = os.listdir(pathVideo)
        print("list_video", self.list_video)

    '''Весь набор функционала'''
    def Swith(self, message):
        print("command: ", message)
        if message == b"run_monitor1":
            self.runVideo()

        if message == b"stop_monitor1":
            print("stopM1")

            while self.pid.poll() is None:  # Force kill if process is still alive
                time.sleep(3)
                os.killpg(self.pid.pid, signal.SIGKILL)

                print("Stop")


    def runVideo(self):
        name = self.list_video[self.count]
        self.pid = subprocess.Popen(["/home/pi/Documents/startVideo.sh", os.path.join(pathVideo, name)])




class klient(Thread, KlientRPI):  #Класс поток
    def __init__(self, sock, eventStop):

        Thread.__init__(self)
        self.sock = sock  # Из грязи в книзи
        self.eventStop = eventStop  # Из грязи в книзи


    def run(self):  # Запуск и остановка потока
        print("___________________Start potok___________________")
        while self.eventStop.is_set():  #

            data = sock.recv(1024)
            if not data:
                continue
            self.Swith(data)
        print("___________________Stop potok___________________")


if __name__ == '__main__':

    sock = socket.socket()  #Создаём сокет
    eventStop = Event()  #Создаём логические сигналы
    eventStop.set()  #True
    while True:
        try:
            try:
                print("Повтор подключения")
                sock.connect(('192.168.1.56', 9090))  #Подключаемся к главному компу
                print('try connect')
            except TimeoutError as e:  #Отлавливаем временную ошибку
                sock = socket.socket()  #Создаём сокет
                print("error " + str(e))
                if "objKlient" in locals():  #Проверяем есть ли переменная objKlient
                    eventStop.clear()  #False
                else:
                    print("objKlient - нет такой переменной")
            else:
                eventStop.set()  # True
                objKlient = klient(sock, eventStop)  #Создаём объект класса и передаём ему аргументы(текущие соединение и сигнал на остановку)

                objKlient.getListVideo()

                objKlient.start()  #Запускаем поток
                objKlient.join()  #Ждёт пока закончится поток(чтобы не перескакивал на след строчку
        except BaseException as be:  ##Отлавливаем базываю ошибку
            sock = socket.socket()  #Создаём сокет
            print("error BE: " + str(be))
            if "objKlient" in locals():  #Проверяем есть ли переменная objKlient
                eventStop.clear()  #False
            else:
                print("objKlient - нет такой переменной")
        else:
            pass
