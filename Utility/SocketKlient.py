import socket
import subprocess
from threading import Thread, Event


pathVideo = r'/home/pi/Videos'  # Путь до папки с видео


class KlientRPI:

    '''Весь набор функционала'''
    def Swith(self, message):
        print("command: ", message)
        if message == b"run_monitor1 ":
            self.setM1()
        else:
            self.setM1()

        if message == b'run_monitor2':
            self.setM2
        else:


    def stopVideoM1(self):
        '''
        Останавливает воспроизведение видео на мониторе 1
        '''
        print('stop_video')

    def setM1(self, mod1:bool):  #Запускает список видео на мониторе №1
        if mod1:
            subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])
            pidM1 = subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo]).pid
            print('runVideoM1',pidM1)
        else:
            print("stopM1")


    def setM2(self,pathVideo, mod2):  #Запускает список видео на мониторе №2
        if mod2 == True:
            subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])
            print('runVideoM2')
        else:
            print("stopM4")

    def setM3(self,pathVideo, mod3):  #Запускает список видео на мониторе №3
        if mod3 == True:
            subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])
            print('runVideoM3')
        else:
            print("stopM3")

    def playProjector(self,pathVideo, mod4):  #Запускает список видео на проекторе
        if mod4 == True:
            subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])
            print('run_projector')
        else:
            print("stopM4")




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
