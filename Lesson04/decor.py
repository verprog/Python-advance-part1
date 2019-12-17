class Shop:

    _total_sales = 0

    def __init__(self, name, sales):
        self._name = name,
        self._sale = self
        Shop._total_sales += sales

    @classmethod
    def get_total_sales(cls):
        # cls == Shop
        return Shop._total_sales

    @staticmethod
    def get_total_static_sales():
        return Shop._total_sales

    def __call__(self, *args, **kwargs):
        print(f'Hi im object {self.__class__.__name__}')


ss = Shop('NN',4000)
ss = Shop('dd',5)
print(ss.get_total_sales())
ss()

class Decorator:

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print(f'Decor {self._func.__name__}')
        self._func()

@Decorator
def fuenc():
    pass

func()