def sum_func(a, b):
    return sum([a, b])

print(sum_func(1, 2))
print('*' * 30)


def sum_func(*args):
    print(*args)
    print(args)


a = [1,2,3,4]
sum_func(a)
sum_func(1,2,3,4)
print('*' * 30)

def s_func(*args):
    result = 0
    for i in args:
        result += i

    return args

a = [1,2,3,4]
s_func(a)
print(s_func(a))