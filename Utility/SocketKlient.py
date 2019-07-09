import socket
import subprocess
from threading import Thread, Event


pathVideo = '/home/pi/Videos'  # Путь до папки с видео


class KlientRPI:
    '''Весь набор функционала'''
    def Swith(self, message):
        print("command: ", message)
        if message == b"run_video":
            self.setM1()
        else:
            self.stopVideoM1()




    def stopVideoM1(self):
        '''
        Останавливает воспроизведение видео на мониторе 1
        '''
        print('stop_video')

    def setM1(self, pathVideo, ):  #Запускает список видео на мониторе №1
        # subprocess.call("sh /home/pi/Documents/startVideo.sh %s" % pathVideo)
        subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])
        print('runVideoM1')

    def stopVideoM2(self):  #Останавливает воспроизведение видео на мониторе 2

        print('stopVideoM2')

    def playVideoM2(self,pathVideo):  #Запускает список видео на мониторе №2
        subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])
        print('playVideoM2')

    def stopVideoM3(self):  #Останавливает воспроизведение видео на мониторе 3
        print('stopVideoM3')

    def playVideoM3(self,pathVideo):  #Запускает список видео на мониторе №3
        subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])

        print('playVideoM3')

    def playProjector(self,pathVideo):  #Запускает список видео на проекторе
        subprocess.call(["/home/pi/Documents/startVideo.sh", pathVideo])

        print('run_projector')

    def stopProjector(self):  #Останавливает воспроизведение видео на проеторе
        print('stop_projector')




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
