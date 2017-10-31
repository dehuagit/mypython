import sys, signal, time


def now():
  return time.asctime()

def onSignal(signum, stackframe):       # python signal handler
  print('Got alarm', signum, 'at', now())  # most handler stay in effet


while True:
  print('Stting at', now())
  signal.signal(signal.SIGALRM, onSignal)    # install signal handler
  signal.alarm(5)
  signal.pause()

