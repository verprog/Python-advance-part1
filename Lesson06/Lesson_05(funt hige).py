
list_of_names = ['ruper','chubaka','lisiy','lyusinda']

def making_upper(string):
    return string.upper()


result = []
#1
for name in list_of_names:
    result.append(making_upper(name))
print(result)
#2
print([making_upper(name) for name in list_of_names])

#3
print(list(map(making_upper, list_of_names)))

#4 lambda
mp = list(map(lambda x, y:(x.upper(), y.lower()), list_of_names,list_of_names))
print(mp)
print('*' * 100)

def func(extra_value,**kwargs):
    for k, v in kwargs:
        if v == extra_value:
            kwargs.pop(k)
            break
    return kwargs


extra_value = 'token'
kwargs = {
    'sum': 12,
    'id': 123,
    'comment': 'bla bla',
    'token': 11111111,
    'brocken': 'token'

}
d1 = dict(filter(lambda k: k[1] != extra_value, kwargs.items()))

print(d1)


