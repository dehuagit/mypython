import os

def child():
  print("Hell from child", os.getpid())
  os._exit(0)

def parent():
    while True:
      newpid = os.fork()
      if newpid == 0:
        child()
      else:
        print('Hello from paraent', os.getpid(), newpid)
      if input() == 'q': break


parent()
