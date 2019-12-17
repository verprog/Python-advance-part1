from abc import ABCMeta, abstractmethod
from datetime import date


def get_age(birthday):
    today = date.today()
    age = today.year - birthday.year
    if today.month < birthday.month:
        age -= 1
    elif today.month == birthday.month and today.day < birthday.day:
        age -= 1
    return age


class Person(metaclass=ABCMeta):

    def __init__(self, name, birthday):
        self._name = name,
        self._birthday = birthday

    @abstractmethod
    def get_info(self):
        return get_age(f'Nmae: {self._name}, age {get_age(self._birthday)})


class Abiturient(Person):

    def __init__(self, name, birthday, last_name, facultet ):
        Person.__init__(self, name, birthday)



atr = Abiturient('Raul', '10.01.2010')
print(atr.get_birthday())