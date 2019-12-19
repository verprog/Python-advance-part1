from threading import Thread
import urllib.request

class MyThread(Thread):

    def __init__(self,arg, deamon, name):
        self._is_running = True
        self._arg = arg
        super().__init__(deamon=deamon, name=name)
    thread1 = Thread(target=self._arg, args=('f1.txt', 200,)

    def run(self):
        while self._is_running:
            print('Working')

def download(urls,file_path):

    print('Beginning file download with urllib2...')
    print(type(file_path))
    urllib.request.urlretrieve(urls, file_path)
    print('done')


url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
ddd = 'C:/Users/Administrator/Downloads/cate.jpg'
# download('http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg',ddd)


for i in range(3):
    MyThread(download, False,f'Download - {i}', {'urls': url,'file_path': ddd}).start()