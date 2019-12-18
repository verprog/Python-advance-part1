print('Задание №1 Stack','\n','*' * 30)


class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return f'Error: stack is empty'

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            return f'Error: stack is empty'

    def size(self):
        return len(self.items)


s = Stack()

print(s.isempty())
s.push('one')
s.push('two')
print(s.peek())
s.push('three')
s.push('four')
print(s.size())
print(s.isempty())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.size())

print('Задание №2 Queue', '\n', '*' * 30)


class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        try:
            return self.items.pop()
        except IndexError:
            return f'Error: queue is empty'

    def size(self):
        return len(self.items)


s = Queue()
s.enqueue('one')
s.enqueue('two')
s.enqueue('three')
print(s.dequeue())
print(s.dequeue())
print(s.dequeue())
print(s.size())
print(s.isempty())


print('Задание №3 Complex number', '\n', '*' * 30)
class Complex():

    def __init__(self, real=0, imag=0):
        self._real = real
        self._imag = imag

    def __repr__(self):
        return f'Complex number: {self._real} + {self._imag}i'

    def __str__(self):
        return f'Complex number: {self._real} + {self._imag}i'

    # Получение вещественной части
    def get_real(self):
        return self._real

    # Получение мнимой части
    def get_imag(self):
        return self._imag

    # Изменение вещественной части
    def set_real(self, real):
        self._real = real

    # Изменение мнимой части
    def set_imag(self, imag):
        self._imag = imag

    # Перезагрузка операторов
    def __add__(self, other):
        return Complex(self._real + other._real, self._imag + other._imag)

    def __sub__(self, other):
        return Complex(self._real + (-other._real), self._imag + (-other._imag))

    def __mul__(self, other):
        return Complex(
                        (self._real * other._real) - (self._imag * other._imag),
                        (self._imag * other._real) + (self._real * other._imag)
                        )

    def __truediv__(self, other):

        try:
            return Complex(
                            ((self._real * other._real) + (self._imag * other._imag)) / ((other._real ** 2) + (other._imag ** 2)),
                            ((self._imag * other._real) - (self._real * other._imag)) / ((other._real ** 2) + (other._imag ** 2))
                            )
        except   ZeroDivisionError:
            return ('Error: Division by zero!')


compl_1 = Complex(1, 2)
compl_2 = Complex(3, 2)

cmplx_plus = compl_2 + compl_1
cmplx_minus = compl_2 - compl_1
cmplx_div = compl_2 / compl_1
cmplx_mul = compl_2 * compl_1

print(f'Суммируем  : {cmplx_plus}')
print(f'Вычитаем : {cmplx_minus}')
print(f'Деление : {cmplx_div}')
print(f'Умножение : {cmplx_mul}')
