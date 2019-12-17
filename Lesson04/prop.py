class Dot:

    def __init__(self, x , y):
        self._x = x,
        self._y = y
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value <0:
            print('error')
            self._x = 0
            return None
        else:
            self._x = value
            return self._x


        # def set_x(self, value):
    #     self._x = value
    #
    # def get_x(self):
    #     return self._x
    #
    # def set_y(self, value):
    #     self._y = value
    #
    # def get_y(self):
    #     return self._y

obj = Dot(1,2)

print(obj.x)


obj.x = 20
print(obj.x)