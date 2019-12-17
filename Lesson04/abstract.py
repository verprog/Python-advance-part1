from abc import ABC, abstractmethod


class Vhicle(ABC):

    attr = 1
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def beep(self):
        print('def beep')

class Car(Vhicle):

    def move(self):
        print('moving')

    def beep(self):
        print('beep')

print((Vhicle))

Car().move()
Car().beep()


class MyABC:

    def my_method(self):
        raise NotImplementedError


class MyClass(MyABC):
    pass