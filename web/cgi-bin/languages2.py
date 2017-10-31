#!/usr/bin/python


REPLY = """Content-type: text/html

<html>
<title>Language2</title>

<body>
To see the code generates is page and reply, click
<a href="getfile.py?filename=cgi-bin/languages2.py">here</a>
<a href="getfile.py?filename=cgi-bin/languages2common.py">here</a>


<hr>
<form method=POST action="languages2reply.py">
  <select name=%s>
    <option>All
    %s
    <option>Other
    <p><input type=submit>
</form>

</body>
</thml>
"""


from languages2common import hellos, inputkey
options = []
for lang in hellos:
  options.append('<option>' + lang)
options='\n\t'.join(options)
print(REPLY %(inputkey, options))






