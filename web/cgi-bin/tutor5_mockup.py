#!/usr/bin/env python

import cgi, sys
from formMockup import formMockup

form = formMockup(name='Bob',
                  shoesize='Small',
                  language=['Python', 'C++', 'HTML'],
                  comment='Ni, NI,ni' 
                 )  # parse form data
print('COntent-type: text/html\n')  # plus blank line

#class dummy:
#  def __init__(self,s): self.value = s
#form = {'user':dummy('bob'), 'age':dummy('10')}

html = """
<h1>greetings</h1>
<hr>
<h4>your name is %(name)s</h4>
<h4>your wear %(shoesize)s shoes</h4>
<h4>your current job: %(job)s</h4>
<h4>your program in  %(language)s</h4>
<h4>you said in  %(comment)s</h4>
</hr>
"""

data = {}
for field in ('name', 'shoesize', 'job', 'language', 'comment'):
  if not field in form:
    data[field] = '(unknown)'
  else:
    if not isinstance(form[field], list):
      data[field] = form[field].value
    else:
      values = [x.value for x in form[field]]
      data[field] = ' and '.join(values)

print(html %(data))



