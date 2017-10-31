#!/usr/bin/env python

import cgi, sys

sys.stderr = sys.stdout  # errors to browser
form = cgi.FieldStorage()  # parse form data

print('COntent-type: text/html\n')  # plus blank line

#class dummy:
#  def __init__(self,s): self.value = s
#form = {'user':dummy('bob'), 'age':dummy('10')}

html = """
<h1>greetings</h1>
<hr>
<h4>%s</h4>
<h4>%s</h4>
<h4>%s</h4>
</hr>
"""


if not 'user' in form:
  line1 = 'Who are you?'
else:
  line1 = 'Hello, %s' % form['user'].value


line2 = "you're talking to a %s server." % sys.platform
#print(cgi.test())

line3 = ""
if 'age' in form:
  try:
    line3 = "your age squre is %d!" % (int(form['age'].value) ** 2)
  except:
    line3 = "sorry, I can't copute %s ** 2" % form['age'].value

print(html %(line1, line2, line3))



