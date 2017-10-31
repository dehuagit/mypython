"""
Porcess class can alos be cubclassess just like thrading.Thread:
  Queue works like queue.Queue but for cross-process, not cross thrad

"""
import os, time, queue
from multiprocessing import Process, Queue   # queue is a pipe +locks/sems

class Counter(Process):
  label = ' @'
  def __init__(self, start, queue):   #retain stat for use in run
    self.state = start
    self.post = queue
    Process.__init__(self)

  def run(self):
    for i in range(3):
      time.sleep(1)
      self.state += 1
      print(self.label, self.pid, self.state)
      self.post.put([self.pid, self.state])
    print(self.label, self.pid, '-')


if __name__ == '__main__':
  print('start', os.getpid())
  expected = 9
  
  post = Queue()
  p = Counter(0, post)
  q = Counter(100, post)
  r = Counter(1000, post)
  p.start(); q.start(); r.start()

  while expected:     # parent consume data on que
    time.sleep(0.5)
    try:
      data = post.get(block=False)
    except queue.Empty:
      print('no data...')
    else:
      print('posted:', data)
      expected -= 1

  p.join();q.join();r.join()
  print('finish', os.getpid(), r.exitcode)



