import time


def decorator(num_repeat):
    def actual_deccorator(func):

        def wrapper(*args):
            start_time = time.time()
            result = []
            for i in range(num_repeat):
                result.append(func(*args))
            print(f">> Function {str(func.__name__).upper()} - execution time: [{round((time.time() - start_time) * 1000, 3)} milliseconds]")

            return result

        return wrapper

    return actual_deccorator


@decorator(4)
def random_generator(range_start, range_end):
    import random
    return random.randint(range_start, range_end)


result = random_generator(10, 50)
print(result)
