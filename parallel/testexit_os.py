def outahere():
  import os
  print('Bye os world')
  os._exit(99)
  print('Never reach')


if __name__ == '__main__': outahere()
