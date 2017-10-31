class error(Exception): pass

class Stack:
  def __init__(self, start=[]):       # self isthe instance object
    self.stack = []         # start is any sequence: stac
    for x in start: self.push(x)
    self.reverse()              # undo push'order reversal

  def push(self, obj):
    self.stack = [obj] + self.stack   # top is frot of list

  def pop(self):
    if not self.stack:
      raise error('underflow')
    top, *self.stack = self.stack
    return top

  def top(self):
    if not self.stack:
      raise error('under flow')
    return self.stack[0]

  def empty(self):      # is mepty ?
    return not self.stack

  # overloads
  def __repr__(self):
    return '[Stack:%s]' % self.stack

  def __eq__(self, other):
    return self.stack == other.stack    # '', !

  def __len__(self):
    return len(self.stack)

  def __add__(self, other):
    return Stack(self.stack + other.stack)    # instace1 _ instacne2

  def __mul__(self, reps):
    return Stack(self.stack * reps)   # instance * reps

  def __getitem__(self, offset):
    return self.stack[offset]     # instace[i], [i:j], in, for

  def __getattr__(self, name):
    return getattr(self.stack, name)    #instace.sort()/reverse()



