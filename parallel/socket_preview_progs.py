from socket_preview import server, client #both use same port number
import sys, os
from threading import Thread


mode = int(sys.argv[1])
if mode == 1:
  server()
elif mode == 2:
  client('ciclient: process = %s' % os.getpid())
else:
  for i in range(5):
    Thread(target=client, args=('client:thread=%s' %i, )).start()







