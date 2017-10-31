import sys, signal, time


def now():
  return time.ctime(time.time()) #current time string


def onSignal(signum, stackframe):       # python signal handler
  print('Got signal', signum, 'at', now())  # most handler stay in effet

signum = int(sys.argv[1])
signal.signal(signum, onSignal)    # install signal handler

while True:
  signal.pause()

