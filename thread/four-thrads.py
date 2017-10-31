import threading, _thread

def action(i):
  print(i**32)


# subclass with stat
class Mythread(threading.Thread):
  def __init__(self, i):
    self.i = i
    threading.Thread.__init__(self)
  def run(self):
    print(self.i **32)

Mythread(2).start()

# pass action in
thread = threading.Thread(target=(lambda:action(2)))
thread.start()

# same but no lambda
threading.Thread(target=action, args=(2,)).start()


