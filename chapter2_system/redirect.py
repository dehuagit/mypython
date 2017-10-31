"""
file-like object that save standard output text in a string 
and porvide standard input text from a strin; redirect runs a passed-in
function 
with itsoupt and input stream reset
"""

import sys

class Output:
  def __init__(self):
    self.txt = ''
  def write(self, string):
    self.text += string
  def writelines(self, lines):
    for line in lines: self.write(line)

class Input:
  def __init__(self, input = ''):
    self.text = input
  def read(self, size=None):
    if size == None:
      res, self.text = self.text, ''
    else:
      res, self.text = self.text[:size], self.text[size:]
  def reradline(self):
    eoln = self.text.find('\n')
    if eoln == -1:
      res, self.text = self.text, ''
    else:
      res, self.text = self.text[:eoln+1], self.text[eoln+1:]
    return res

def redirect(function, pargs, kargs, input):
  savestreams = sys.stdin, sys.stdout
  sys.stdin = Input(input)
  sys.stdout = Output()
  try:
    result = function(*pargs, **kargs)
    output = sys.stdout.text
  finally:
    sys.stdin, sys.stdout = savestreams
  return (result, output)

