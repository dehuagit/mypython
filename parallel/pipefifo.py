import os, time, sys
fifoname = '/tmp/pipefifo' #must open sam ename

def child():
  pipeout = os.open(fifoname, os.O_WRONLY)    #open fifo pipe as fd
  zzz = 0
  while True:
    time.sleep(zzz)     # make parent wait
    msg = ('Spam %03d\n' % zzz).encode()  # pipes are binary bytes
    os.write(pipeout, msg)          #sen to parent
    zzz = (zzz+1) % 5

def parent():
  pipein = open(fifoname, 'r')
  while True:
    line = pipein.readline()[:-1]  # blocks until data send
    print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))

if __name__ == '__main__':
  if not os.path.exists(fifoname):
    os.mkfifo(fifoname)
  if len(sys.argv) == 1:
    parent()
  else:
    child()

