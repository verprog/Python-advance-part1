from threading import Thread

class   MyThread(Thread):

    def __init__(self,arg , deamon, name):
        self._is_running = True
        self._arg = arg
        super().__init__(deamon=deamon, name=name)

    def run(self):
        while self._is_running:
            print('Working')

for i in range(100):
    MyThread(1, False,f'name-{i}').start()