import os
from multiprocessing import Process, Value, Array


procs = 3
count = 0 #per process global, not share


def showdata(label, val, arr):
  msg = '%-12s: pid:%4s, global:%s, value:%s, array:%s'
  print(msg % (label, os.getpid(), count, val.value, list(arr)))

def updater(val, arr):
  global count
  count += 1      #not share
  val.value += 1
  for i in range(3):
    arr[i]+= 1


if __name__ == '__main__':
  scalar = Value('i', 0)  #shared memory: process/thread save
  vector = Array('d', procs) # i for int , d for dobule

  showdata('parent start', scalar, vector)

  # spawn child
  p = Process(target=showdata, args=('child ', scalar, vector))
  p.start()
  p.join()

  print('\nllop1 (updates in parent, serial children)')
  for i in range(procs):
    count += 1
    scalar.value += 1
    vector[i] += 1
    p = Process(target=showdata, args=(('process %s' %i ), scalar, vector))
    p.start()
    p.join()

  print('\nllop2 (updates in parent, parent children)')
  ps = []
  for i in range(procs):
    count += 1
    scalar.value += 1
    vector[i] += 1
    showdata('parent temp', scalar, vector)
    p = Process(target=showdata, args=(('proces %s' %i ), scalar, vector))
    p.start()
    ps.append(p)

  for p in ps:
    p.join()


  print('\nllop3 (updates n searil children)')
  for i in range(procs):
    p = Process(target=updater, args=(scalar, vector) )
    p.start()
    p.join()
  showdata('parent temp', scalar, vector)

  ps = []
  print('\nllop4  (updates n parent children)')
  for i in range(procs):
    p = Process(target=updater, args=(scalar, vector) )
    p.start()
    ps.append(p)
  
  for p in ps:
    p.join()

  showdata('parent end', scalar, vector)

