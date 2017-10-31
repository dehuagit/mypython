#!/usr/bin/env python


print( """Content-type: text/html

<TITLE>CGI 101</TITLE>
<H1> A Second CGIScript </H1>
<HR>

<P>Hello CGI World</P>
<HR>
<table border=1>
""")

for i in range(5):
  print('<tr>')
  for j in range(4):
    print('<td>%d.%d</td>' % (i,j))
  print('</tr>')
 

print("""</table>>""")






