#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()  # parse form data
print('Content-type: text/html\n') #plus blak line


html = """
<h1> Greetings</h1>
<hr>

<p>%s</p>
"""



if not 'user' in form:
  print(html % 'who are your?')
else:
  print (html % ('Hello, %s.' % form['user'].value))







