#!/usr/bin/python
import cgi,os, sys

formatted = False   # True=wrap text in HTML
privates = ['../client/http-getfile.py']   #donteshowthisi

try:
  samefile = os.path.samefile
except:
  def samefile(path1, path2):
    apath1 = os.path.abspath(path1).lower()
    apath2 = os.path.abspath(path2).lower()
    return apth1 == apath2

html = """
<html>
<title>Getfile response</title>
<h1>source code for '%s' </h1>
<hr>
<pre>%s</pre>
</html>
"""

def restricted(filename):
  for path in privates:
    if samefile(path, filename):    #  all paths by os.stat
      return True

try:
  form = cgi.FieldStorage()
  filename = form['filename'].value
except:
  filename = 'cgi-bin/getfile.py'

try:
  assert not restricted(filename)
  filetext = open(filename).read()
except AssertionError:
  filetext = '(File access denied)'
except:
  filetext = '(Error opening file: %s)' % sys.exc_info()[1]

if not formatted:
  print('Content-type: text/plain\n') # send plain text
  print(filetext)
else:
  print('Content-type: text/html\n')
  print(html % (filename, cgi.escape(filetext)))
