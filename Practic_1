# задание 1
list_1 = range(50)

for i in list_1:
    if i % 2 == 0 and i != 0:
        print(i)

print('*' * 30)


# задание 2
dict_1={'Украина':'Киев',
        'Россия':'Москва',
        'Беларусь':'Минск',
        }
list_can = ('Украина', 'Россия', 'Беларусь', 'Аргентина')


for  strana, gorod in dict_1.items():
    if strana in list_can:
        print(strana, gorod)

print('*' * 30)


# задание 3
list_2 = range(100)
for i in list_2:
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print('*' * 30)


# задание4
def bank(sum_dep, count_year, perc):
    if int(sum_dep) and int(count_year) and count_year > 0 and int(perc):
        data = sum_dep*(perc/100+1)
        for i in range(count_year-1):
            data = data*(perc/100+1)
    else:
        print('Error input values')
    return round(data,3)


print(bank(100, 1, 10.5))
