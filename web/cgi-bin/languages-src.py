#!/usr/bin/python

import cgi

filename = 'cgi-bin/languages.py'

print('Content-type: text/html\n')
print('<TITLE>Languages</title>')
print("<h1>source code: %s </h1>" % filename)
print('<hr><pre>')
print(cgi.escape(open(filename).read()))
print('</pre>')

