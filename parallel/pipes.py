import os,sys

def spawn(prog, *args): # pass progranmae, cmdline args
  stdinFd = sys.stdin.fileno()
  stdoutFd = sys.stdout.fileno()

  parentStdin, childStdout = os.pipe()
  childStdin, parentStdout = os.pipe()
  pid = os.fork()
  if pid:   #parent 
      os.close(childStdout)
      os.close(childStdin)
      os.dup2(parentStdin, stdinFd) # my sys.stdin copy = pipe1[0]
      os.dup2(parentStdout, stdoutFd) #my sys.stdout copy = pipe2[1]
  else:
    os.close(parentStdin)
    os.close(parentStdout)
    os.dup2(childStdin, stdinFd)
    os.dup2(childStdout, stdoutFd)
    args = (prog,) + args
    os.execvp(prog, args)   # new program in this process
    assert False, 'execvp failed!'  #os.exec call never returns here

if __name__ == '__main__':
  mypid = os.getpid()
  spawn('python', 'pipes-testchild.py', 'spam')

  print("Hello 1 from parent", mypid)
  sys.stdout.flush()
  reply = input()
  sys.stderr.write('Parent got: "%s"\n' % reply)
  
  print('Hello 2 from parent', mypid)
  sys.stdout.flush()
  reply = sys.stdin.readline()
  sys.stderr.write('Parent got: "%s"\n' % reply[:-1])

