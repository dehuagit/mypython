#!/usr/bin/python



debugme  = False
inputkey = 'language'


hellos = {
  'Python': r"print(Hello workd)" ,
  'Python2': r"print 'Hello world'",
  'Perl': r" print 'Hello world\n'",
  'Java': r'System.out.println("helloworld")',
  'C': r'printf("hello world")',
  'C++': r'count << "hello  world <<endl"'
}

class dummy:
    def __init__(self, str): self.value = str



import cgi, sys

if debugme:
  form = {inputkey: dummy(sys.argv[1])}
else:
  form = cgi.FieldStorage()


print('Content-type: text/html\n')
print('<TITLE>II</TITLE>')

def showHello(form):
  choice = form[inputkey].value
  print('<h3>%s</h3><p><PRE>' % choice)
  try:
    print(cgi.escape(hellos[choice]))
  except:
    print("Sorry I don't know that language")
  print('</PRE></P><BR>')
  
if not inputkey in form or form[inputkey].value == 'All':
  for lang in hellos.keys():
    mock = {inputkey: dummy(lang)}
    showHello(mock)
else:
  showHello(form)

print('<HR>')
