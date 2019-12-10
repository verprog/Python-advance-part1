
class Cat:
    def __init__(self, name):
        self._name = name
    def meow(self):
        print('Meow!')
    def say_my_name(self):
        print(f'My name is {self._name}')

    def __add__(obj1, obj2):
        return Cat(obj1._name + obj2._name)

def my_func():
    print('Hello')

print(my_func)

def another_func(func1):
    func1()

another_func(my_func)


print('*' * 30)

cat1=Cat('Rumba')
cat2=Cat('Burumba')

cat3=cat1+cat2

print(cat3.say_my_name())

print('*' * 30)

def square_root(number):
    return number ** 2

lambda number: number ** 2

a = lambda number: number ** 2
print(a(2))

print('*' * 30)

b = map(lambda number: number ** 2, range(100))
print(list(b))