import sys, time
from select import select
from socket import *

def now(): return time.ctime(time.time())

myHost = ''
myPort = 50007
if len(sys.argv) == 3:      # aloow host/port as cmdlilne args too
  myHost, myPort = sys.argv[1:]
numPortSocks = 2

# make main sockets for accepting new client requests
mainsocks, readsocks, writesocks = [], [], []
for i in range(numPortSocks):
  portsock = socket(AF_INET, SOCK_STREAM)   # mak TCP/IP socket object
  portsock.bind((myHost, myPort))
  portsock.listen(5)
  mainsocks.append(portsock)    # add to main list to identify
  readsocks.append(portsock)  # add to select inputs list
  myPort += 1

# vent lop: listen and multipxex until server porcess killed
print('select-server loop starting')
while True:
  readables, writeables, exceptions = select(readsocks, writesocks, [])
  for sockobj in readables:
    # port socket: accept new client
    if sockobj in mainsocks:      # for ready input sockets
      newsock, address = sockobj.accept()
      print('Connect:', address, id(newsock))
      readsocks.append(newsock)
    else:
      ## client socket:  read next line
      data = sockobj.recv(1024)
      print('\tgot', data, 'on', id(sockobj))
      if not data:
        sockobj.close()
        readsocks.remove(sockobj)
      else:
        # his my block: sholud really select tor wirtes too
        reply = 'Echo->%s at %s' % (data, now())
        sockobj.send(reply.encode())




