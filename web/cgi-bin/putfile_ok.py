#!/usr/bin/python

"""
Extract file uploaded by http from brows, ths may only work 
fi file or dir is writable: a unix 'chmod 777 puloads'
my suffice

caveat: since file content always str from the cgi module, but this is a
temporary solution anyhow-- cgi module does't handle binary file upload in 3.1
at all

"""


import cgi, os

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['clientfile']

print("COntent-type: text/html\n")

# Test if the file was uploaded
if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('uploads/' + fn, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'

html = """
<html><body>
<p>%s</p>
</body></html>
"""


print( html % message )
