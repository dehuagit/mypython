

import os
from multiprocessing import Process, Pipe

def sender(pipe):
  pipe.send(['spam'] + [42, 'eggs'])
  pipe.close()

def talker(pipe):
  pipe.send(dict(name='bob', spam=42))
  reply = pipe.recv()     # onl wait client send
  print('talker got:', reply)

if __name__ == '__main__':
  (parentEnd, childEnd) = Pipe()
  Process(target = sender, args = (childEnd,)).start()  #spawn child with pipe
  print('parent got:', parentEnd.recv()) #receive from child
  parentEnd.close()
    #or aut-close
  (parentEnd, childEnd) = Pipe()
  child = Process(target = talker, args = (childEnd,))
  child.start()
  print('parent got:', parentEnd.recv())
  parentEnd.send({x * 2 for x in 'spam'})
  child.join()
  print('parent exit')

