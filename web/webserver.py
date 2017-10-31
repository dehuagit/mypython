#!/usr/bin/env ptyhon
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'    # whre html file and cgi-bin script directory live
port = 80

if len(sys.argv) > 1: webdir = sys.argv[1]
if len(sys.argv) > 2: port = int(sys.argv[2])
print('webdir "%s", port %s' % (webdir, port))

os.chdir(webdir)
srvraddr = ('192.168.24.108',port)
#srvraddr = ('',port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
