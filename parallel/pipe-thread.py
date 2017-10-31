import os, time, threading

def child(pipeout):
  zzz = 0
  while True:
    time.sleep(zzz)     # make parent wait
    msg = ('Spam %03d' % zzz).encode()  # pipes are binary bytes
    os.write(pipeout, msg)          #sen to parent
    zzz = (zzz+1) % 5


def parent(pipein):
    while True:
      line = os.read(pipein, 32)  # blocks until data send
      print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


pipein, pipeout = os.pipe()     # make 2 -end pipe
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)

