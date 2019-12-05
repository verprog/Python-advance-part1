list_1=[1,2,3,4,5]
list_2=list([1,2,3,4])
print(list_1[0])
list_1[0]='zero'
print(list_1[0])


tuple_1=(1,2,3,4)
print(tuple_1[0])

dict_1={'one':1,
        'two':2,
        (1,2):3,
        'tree':[1,2,3]
        }
print(dict_1.get((1,3),-1))

print(set([1,2,3,2,3,4]))

print(hash('00'))

print(bool(1))
print(bool(0))


user_string = input('enter')

if user_string:
    print(user_string[::-1])
else:
    print('Empty')

if user_string:
    print(user_string[::-1])

elif True:
    pass
else:
    print('Empty')

number=int(input('enter number'))

if number>100:
    print('> 100')
else:
    print('notttt')

result = '>100' if number>100 else None



22222

i = 0
while i<100:
    print(i)
    i += 1
    if i==50:
        break
        continue


list_2 = [1,2,3,4,5,6,7,8]
list_2 = range(0,100,10)
len_of_list = len(list_2)

for ind in list_2:
    print(ind)

for ind, dt in enumerate(list_2[1:50]):
    print(ind,dt)

dict_1={'one':1,
        'two':2,
        (1,2):3,
        'tree':[1,2,3]
        }

# for item in dict_1.values():
for item,dd in dict_1.items():
    print(item,dd)

print('*' * 20)

try:
    b = 1 + 'ff'
    a = 10/0
except (ZeroDivisionError, TypeError) as e:
    a = None
    print(e.args)
else:
    print('normal data')
finally:
    print('bay')
