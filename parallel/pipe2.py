
import os, time

def child(pipeout):
  zzz = 0
  while True:
    time.sleep(zzz)     # make parent wait
    msg = ('Spam %03d\n' % zzz).encode()  # pipes are binary bytes
    os.write(pipeout, msg)          #sen to parent
    zzz = (zzz+1) % 5


def parent():
  pipein, pipeout = os.pipe()     # make 2 -end pipe
  if os.fork() == 0:
    os.close(pipein)
    child(pipeout)
  else:
    os.close(pipeout)
    pipein = os.fdopen(pipein)
    while True:
      line = pipein.readline()[:-1]  # blocks until data send
      print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))

parent()

