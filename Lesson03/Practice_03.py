import time
def decorator(num_repeat):
    def actual_deccorator(func):

        def wrapper(range_start, range_end):
            start_time = time.process_time()
            result = []
            for i in range(num_repeat):
                result.append(func(range_start, range_end))

                # def __new__(cls, *args, **kwargs):
                #     obj = super().__new__(cls, *args, **kwargs)
                #     return obj

            print('Elapsed time during the whole function in seconds: ', time.process_time() - start_time)
            return result

        return wrapper
        # total_time = time_start-time.time()
    return actual_deccorator



@decorator(5)
def random_generator(range_start, range_end):
    import random
    return random.randint(range_start, range_end)


result= random_generator(10,50)
print(result)



# Домашка - что такое стек, очередь, комлексное число реальная и мнимая часть