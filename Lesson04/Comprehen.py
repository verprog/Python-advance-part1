import time

start = time.time()
a = []

for i in range(100):
    if i % 2 == 0:
        a.append(i)

end = time.time() - start


start_compr = time.time()
odds = [(i,i) for i in range(100) if i % 2 == 0]
print(odds)
end_compr = time.time() - start_compr

if end_compr< end:
    print('Comperhessions are faster')

print(end)
print(end_compr)

dict = {1:2,
        2:3,
        3:4}

dics = [(i,j) for i, j in dict.items()]

print(dics)