#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()   # parse form data
print('Content-type: text/html\n')
print('<title>ReplyPage</title>')

if not 'user' in form:
    print('<h1>Who are your</h1>')
else:
    print('<h1>Hello %s!</h1>' % cgi.escape(form['user'].value))
