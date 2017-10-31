import _thread as thread, time

def counter(myId, count):
  print("count", count)
  for i in range(count):
    print('[%s] = > %s' % (myId, i))

for i in range(20):
  thread.start_new_thread(counter, (i,15))


time.sleep(15)
print('Main thread')

