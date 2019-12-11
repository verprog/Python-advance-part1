def decorator(num_repeat):

    def actual_deccorator(func):

        def wrapper(range_start, range_end):
            result = []
            for i in range(num_repeat):
                result.append(func(range_start, range_end))

            return result

        return wrapper

    return actual_deccorator

# @deccorator(num_of_repeats)

# result = deccorator(10)(random_generator(10,50))

@decorator(5)
def random_generator(range_start, range_end):
    import random
    return random.randint(range_start, range_end)

result = random_generator(10,50)
print(result)


print('*' * 30)

class Singleton:

    _objects = None
    def __new__(cls, *args, **kwargs):

        if cls._objects:
            return cls._objects
            # raise Exception('obj exists')

        obj = super().__new__(cls, *args, **kwargs)
        cls._objects = obj
        return obj

obj_1 = Singleton()
print(obj_1)
obj_2 = Singleton()
print(obj_2)