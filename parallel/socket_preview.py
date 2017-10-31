from socket import socket, AF_INET, SOCK_STREAM

port = 50008
host = 'localhost'

def server():
    sock = socket(AF_INET, SOCK_STREAM)  # ip addressed tcp connection
    sock.bind(('', port))       # ind too port on this machine
    sock.listen(5)        # allow up 5 pedning clients
    while True:
      conn, addr = sock.accept()    #wait for client to connect
      data = conn.recv(1024)    #  read bytes data from this client
      reply = 'server got:[%s]' % data
      conn.send(reply.encode())

def client(name):
  sock = socket(AF_INET, SOCK_STREAM)
  sock.connect((host, port))
  sock.send(name.encode())
  reply = sock.recv(1024)
  sock.close()
  print('client got:[%s]' % reply)

if __name__ == '__main__':
  from  threading import Thread
  sthread = Thread(target = server)
  sthread.daemon = True   # don't wait for server thread
  sthread.start()     #
  for i in range(5):
    Thread(target = client, args=('chient%s' % i, )).start()








