# Curyingexample

def a(a_arg):
    print(a_arg)

    def b(b_arg):
        print(b_arg)

        def c(c_arg):
            print(c_arg)
            print('end')

        return c

    return b

a(10)(20)(30)

# Decorator

#
#
# def func1(func):
#     print('Hello')
#     print('start func')
#     func()
#     print('ended')
#
#
# a=func1(random_generator())


print('*' * 30)
def decorator(func):

    def wrapper(range_start, range_end):
        print('start')
        result = func(range_start, range_end)
        print(f'result is {result}')
        print('end')

        return result

    return wrapper


# result = decorator(random_generator)(100,200)

@decorator
def random_generator(range_start, range_end):
    import random
    return random.randint(range_start, range_end)

# with @ syntax
result = random_generator(100, 200)
print('*' * 30)
# without @ syntax
result1 = decorator(random_generator)(100, 200)


