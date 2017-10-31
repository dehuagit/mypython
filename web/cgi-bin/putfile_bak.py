#!/usr/bin/python

"""
Extract file uploaded by http from brows, ths may only work 
fi file or dir is writable: a unix 'chmod 777 puloads'
my suffice

caveat: since file content always str from the cgi module, but this is a
temporary solution anyhow-- cgi module does't handle binary file upload in 3.1
at all

"""


import cgi, os, sys
import posixpath, ntpath,macpath #for client path


debugmode = True # True = print form info
loadtextauto = True  # True = read file at once
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
<p> <pre>%s</pre>
</p>
"""



# porcess form data

def splitpath(origpath):                            # get file at end
  for pathmodule in [posixpath, ntpath, macpath]:  # try all client
    basename = pathmodule.split(origpath)[1]      # may be any server
    if basename != origpath:
      return basename                       # lets spacess pass
  return origpath                   # failed or no dirs

def saveonserver(fileinfo):     # use file input form data
  basename = splitpath(fileinfo.filename)   # name without dir path
  srvrname = os.path.join(uploaddir, basename) # store in a dir if set
  srvrfile = open(srvrname, 'wb')       # alway write bytes here
  if loadtextauto:
    filetext = fileinfo.value     # reads text into string
    if isinstance(filetext, str):
      filedata = filetext.encode()
      srvrfile.write(filedata)        # save in server file
    else:
      print("file is not strcontent!!")
      srvfile.write(fileinfo.file.read())
      #for chunk in fbuffer(fileinfo.file):
       # print("chunk")
        #srvrfile.write(chunk)
  else:                           # else read line by line
    numlines, filetext = 0, ''
    while True:
      line = fileinfo.file.readline()
      if not line: break
      if isinstance(line, str):
        line = line.encode()
      srvrfile.write(line)
      filetext += line.decode()
      numlines += 1
    filetext = ('[Lines=%d]\n' % numlines) + filetext
  srvrfile.close()
  os.chmod(srvrname,0o666)    # make writable: owned by nobdy
  return filetext, srvrname


def main():
    if not 'clientfile' in form:
      print(html % 'Error: on file was received')
    elif not form['clientfile'].filename:
      print(html % 'Error: filname is missing')
    else:
      fileinfo = form['clientfile']
      try:
        filetext, srvrname = saveonserver(fileinfo)
      except:
        errmsg = '<h2 Error</h2><p>%s<p>%s' % tuple(sys.exc_info()[:2])
      else:
        print(goodhtml % (cgi.escape(fileinfo.filename), cgi.escape(srvrname),                                                                    cgi.escape(filetext)))


main()



