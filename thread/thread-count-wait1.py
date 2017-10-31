import _thread as thread, time

exitmutexes = [thread.allocate_lock() for i in range(10)]



def counter(myId, count):
  for i in range(count):
    time.sleep(2)
    print('[%s] = > %s' % (myId, i))
  exitmutexes[myId].acquire()     #signal main thread

for i in range(10):
  thread.start_new_thread(counter, (i,100))


for mutex in exitmutexes:
  while not mutex.locked(): pass

print('Main thread')

