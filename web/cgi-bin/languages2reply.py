#!/usr/bin/python


import cgi, sys
from formMockup import FieldMockup
from languages2common import hellos, inputkey
import formMockup

debugme=False

hdrhtml = """Content-type: text/html\n
<TITLE>LANGUAGE</TITLE>
<h1>Syntax</H1>
"""

langhtml = """
<h3>%s</h3>
<pre>
%s
</pre>
</p>
<br>
"""

def showHello(form):  # for one language
    choice = form[inputkey].value
    try:
      print(langhtml %(cgi.escape(choice), cgi.escape(hellos[choice])))
    except:
      print(langhtml %(cgi.escape(choice), "sorry-Idon't know that language"))

import sys
def main():
  if debugme:
    form = {inputkey:FieldMockup(sys.argv[1])}
  else:
    form = cgi.FieldStorage()

  print(hdrhtml)
  if not inputkey in form or form[inputkey].value == 'All':
    for lang in hellos.keys():
      mock = {inputkey: FieldMockup(lang)}
      showHello(mock)
  else:
      showHello(form)
  print('<HR>')
  print('python version:', sys.version_info)


if __name__ == '__main__':
  main()

