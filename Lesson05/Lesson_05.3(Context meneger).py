with open('file.txt', 'w') as file:
    print(file)

# file = open('file.txt', 'w')
# file.close()


class MyContextManager:

    def __init__(self, number):
        self._number = number

    def __enter__(self):
        print('Context menager open')
        return self._number

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        self._number = 0


a = MyContextManager(10)
with a as num:
    print(num)

print(a._number)