class MyList:

    def __init__(self, *list_):
        self._list = list_
        # self._size = len(self._list)

    def __getitem__(self, index):
        # self._check_range(index)
        return self(index)

    # def __setitem__(self, index, value):
    #     self._check_range(index)
    #     self._array[index] = value
    #
    # def _check_range(self, index):
    #     if index < 0 or index > self._size:
    #         raise IndexError
    #
    # def __len__(self):
    #     return self._size
    #
    # @property
    # def head(self):
    #     # -- self._array[0]
    #     return self[0]
    #
    # @property
    # def tail(self):
    #     return self[self._size]

    # def __str__(self):
    #     return self

a = MyList(1,2,3)
print(a[1])
