class FromMeta:
    def hello(self):
        print('Hello')

class UpperCaseMetaClass(type):
    def __new__(cls, name, base, attrs):
        # print(name, base, attrs)
        for i in range(5):
            base = (FromMeta,)
            attrs.update({'var_' + str(i): i})
        return super().__new__(cls, name, base, attrs)

class MyClass(metaclass=UpperCaseMetaClass):

    _attribute_of_class = 'Attr'
    def __init__(self, x, y):
        self._x = x,
        self._y = y

# a = MyClass(1,2)
print(dir(MyClass))
print(MyClass.__bases__) #
MyClass(1,2).hello()