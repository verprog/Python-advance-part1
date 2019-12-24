
def counter(start, end):

    while start < end:
            yield start
            start += 1
            print('I am gen func')

obj = counter(0,100)

# for i in obj:
#     print(i)

ic = iter(obj)

print(next(ic))

# >> list comprehension [x for x in range(100)] no GENERATOR

gen_obj = (x for x in range(100))

print(gen_obj)

# ***********************
def randomizer(steps):
    import random
    current_step = 0
    value = 0

    while current_step < steps:
        value += random.random()
        current_step += 1
        yield value

for i in randomizer(10):
    print(i)
