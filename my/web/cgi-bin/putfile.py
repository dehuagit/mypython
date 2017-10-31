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
<p>Your  file, '%s', has been saved on the server as '%s'. </p>
<h2>Analsys ID:  <font color='red'>%s</font><h2>
<hr>
"""

analysishtml = """

<h1>Next Step: analysis</h1>
<form method=get action="analysis.py">
<input type=hidden name=%s value="%s"> <!-- Anaylysis -->
<input type=hidden name=%s value="%s"> <!-- llbrary name-->
<input type=hidden name=%s value="%s"> <!-- Lab3l 1 name-->
<input type=hidden name=%s value="%s"> <!-- label 1 file-->
<input type=hidden name=%s value="%s"> <!-- Label 2 name -->
<input type=hidden name=%s value="%s"> <!-- Label 2 filename-->
<input type=submit value=Analysis>
</form>

"""




# porcess form data
def saveonserver(projectname, fileinfo):     # use file input form data
  basename = fileinfo.filename   # name without dir path
  uploadProjectDir = os.path.join(uploaddir, projectname)
  try:
    os.mkdir(uploadProjectDir)
  except FileExistsError:
    pass
  srvrname = os.path.join(uploadProjectDir, basename) # store in a dir if set
#  print("1 filename:" + srvrname + "<br>")
  srvrfile = open(srvrname, 'wb')       # alway write bytes here
  content = fileinfo.file.read()
  srvrfile.write(content)
  srvrfile.close()
  os.chmod(srvrname,0o666)    # make writable: owned by nobdy
  return srvrname

def safestring(data):
  import string
  allowed = string.ascii_letters + string.digits + '_'
  x = [ c for c in data if c in allowed ]
  return ''.join(x)

from common import *

def main():
  allErrorMessage = ""

  # Data check
  for field in (inputAnakey, inputR1key, inputR2key, inputLibrarykey, inputLabel1key, inputLabel2key):
    if not field in form:
      allErrorMessage += cgi.escape("Error: no '%s' filed . " % field) + "<br>"
    elif not form[field].value:
      allErrorMessage += cgi.escape("Error: no '%s' data. " % field) + "<br>"

  if allErrorMessage:
    print(html % allErrorMessage)
  else:
    AnaName = safestring(form[inputAnakey].value)
    label1 = safestring(form[inputLabel1key].value)
    label2 = safestring(form[inputLabel2key].value)
    R1FileInfo = form[inputR1key]
    R2FileInfo = form[inputR2key]
    libraryInfo = form[inputLibrarykey]
    try:
      servername1 = saveonserver(AnaName, R1FileInfo)
      servername2 = saveonserver(AnaName, R2FileInfo)
      serverLibrary = saveonserver(AnaName, libraryInfo)
    except:
      errmsg = '<h2 Error</h2><p>%s<p>%s' % tuple(sys.exc_info()[:2])
      print(html % errmsg)
    else:
      print(goodhtml % (cgi.escape(R1FileInfo.filename + ", " +
                                   R2FileInfo.filename + "," +
                                   libraryInfo.filename),
                        cgi.escape(servername1 + ", " + servername2 + ", " +
                                   serverLibrary),
                        cgi.escape(AnaName + ", Label: " + label1 + ", " + label2 )))
      print(analysishtml % (inputAnakey, cgi.escape(AnaName),
                            inputLibrarykey, cgi.escape(libraryInfo.filename),
                            inputLabel1key, cgi.escape(label1),
                            inputR1key, cgi.escape(R1FileInfo.filename),
                            inputLabel2key, cgi.escape(label2),
                            inputR2key, cgi.escape(R2FileInfo.filename)))

main()



