import os, time,sys
from socket import *

myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

def now():
  return time.ctime(time.time())

activeChildren = []
def reapChildren():
  while activeChildren:
    pid, stat = os.waitpid(0, os.WNOHANG)
    if not pid: break
    activeChildren.remove(pid)

def handleClient(connection):
  time.sleep(5)
  while True:
    data = connection.recv(1024)
    if not data: break
    reply = 'Echo=>%s at %s' % (data, now())
    connection.send(reply.encode())
  connection.close()
  os._exit(0)

def dispatcher():     # listen until porcess killed
  while True:
    connection, address = sockobj.accept()
    print('Server connected by', address, end=' ')
    print('at', now())
    reapChildren()        # clean up exited children now
    childPid = os.fork()
    if childPid == 0:     # if child process; andle
      handleClient(connection)
    else:                   
      activeChildren.append(childPid)

dispatcher()


