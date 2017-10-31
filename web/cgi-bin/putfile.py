#!/usr/bin/python

import cgi, os, sys


debugmode = False # True = print form info
uploaddir = './uploads'

sys.stderr = sys.stdout # show error msgs
form = cgi.FieldStorage()
print("Content-type: text/html\n")

if debugmode: cgi.print_form(form)

# html templates

html = """
<html>
<title>Putfile response page</title>
<body>

<h1>putfile response page</h1>
%s
</body>
</html>
"""

goodhtml = html % """
<p>Your  file, '%s', has been saved on the server as '%s'.
<p>An echo of the file's contents received and saved appear below
</p>
<hr>
</p>
"""

# porcess form data
def saveonserver(fileinfo):     # use file input form data
  basename = fileinfo.filename   # name without dir path
  srvrname = os.path.join(uploaddir, basename) # store in a dir if set
  print("1 filename:" + srvrname + "<br>")
  srvrfile = open(srvrname, 'wb')       # alway write bytes here
  print("loadauto file+ <br>")
  content = fileinfo.file.read()
  srvrfile.write(content)
  srvrfile.close()
  os.chmod(srvrname,0o666)    # make writable: owned by nobdy
  return srvrname


def main():
    if not 'clientfile' in form:
      print(html % 'Error: on file was received')
    elif not form['clientfile'].filename:
      print(html % 'Error: filname is missing')
    else:
      fileinfo = form['clientfile']
      try:
        srvrname = saveonserver(fileinfo)
      except:
        errmsg = '<h2 Error</h2><p>%s<p>%s' % tuple(sys.exc_info()[:2])
      else:
        print(goodhtml % (cgi.escape(fileinfo.filename), cgi.escape(srvrname)))

main()



