import sys, http.client

showlines = 6

try:
  servername, filename = sys.argv[1:]
except:
  servername, filename = 'www.google.com.tw', '/index.html'

print(servername, filename)
server = http.client.HTTPConnection(servername)
server.putrequest('GET', filename)      # send request and headers
server.putheader('Accept', 'text/html'),  # POST requests work here too
server.endheaders()     # as do CGI  scripter

reply = server.getresponse()
if reply.status != 200:
  print('Error send request', reply.status, reply.reason)
else:
  data = reply.readlines()
  reply.close()
  for line in data[:showlines]:
    print(line)





