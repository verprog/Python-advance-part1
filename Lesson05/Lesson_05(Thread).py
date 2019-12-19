from threading import Thread
import time

def testing_threads():
    # print('Func call')
    time.sleep(0.1)

# sinc
start = time.time()
for i in range(20):
    testing_threads()

print(time.time()-start)


# parallel
start2 = time.time()
for i in range(20):
    t = Thread(target=testing_threads, name = f'MyThread- {i}')
    t.start()
    # print(t.name)

print(time.time()-start2)


thread_list = []
# parallel in list
start2 = time.time()
for i in range(20):
    t = Thread(target=testing_threads, name=f'MyThread- {i}')
    thread_list.append(t)

for i in thread_list:
    print(i.start())

print(time.time()-start2)


t = Thread(target=testing_threads, daemon=True)
t.start()
t.join()
print(t.is_alive())
print('Main Thread','\n', '*' * 30)

