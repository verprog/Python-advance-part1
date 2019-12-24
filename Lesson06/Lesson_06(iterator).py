# list_1 = [1,2,3,4]
#
# list_1_iter = iter(list_1)
# (next(list_1_iter))

# class Starter:
#
#     def __init__(self, start, end):
#         self._start = start
#         self._end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         # if self._start<self._end:
#         #     self._start += 1
#         #     return self._start
#
#         if self._start<self._end:
#             self._start += 1
#             return self._start
#         raise StopIteration()


# class MyIter:
#
#     def __init__(self, start, end):
#         # self._start = start
#         # self._end = end
#         self._starter = Starter(start, end)
#
#     def __iter__(self):
#         return self._starter.__iter__()

    # def __next__(self):
    #     # if self._start<self._end:
    #     #     self._start += 1
    #     #     return self._start
    #
    #     if self._starter._start<self._starter._end:
    #         self._starter._start += 1
    #         return self._starter._start
    #     raise StopIteration()


# obj = MyIter(0, 4)
#
# obj_iter = iter(obj)
#
# # print(next(obj_iter))
# # print(next(obj_iter))
# # print(next(obj_iter))
# # print(next(obj_iter))
#
# for i in obj:
#     print(i)

import random
class Randomizer:

    def __init__(self, steps=0):
        self._steps = steps
        self._current_step = 0
        self._value = 0

    def __iter__(self):
        return self

    def __next__(self):
        # if self._start<self._end:
        #     self._start += 1
        #     return self._start

        if self._current_step>=self._steps:
            self._value += random.random()
            self._current_step += 1
        else:
            raise StopIteration()
        return self._value

obj = Randomizer(100)

for i in obj:
    print(i)