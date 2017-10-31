#!/usr/bin/env python

import cgi,sys,os
from common import *

uploaddir = "./uploads"
sys.stderr = sys.stdout
debugmode = False

if debugmode:
  class dummy:
    def __init__(self,s): self.value = s
  form = {'AnaName':dummy('test') }
else:
  form = cgi.FieldStorage()


print("Content-type: text/html\n")
html="""
<h1>Download list</h1>
<p>Analysis name: %s </p>
"""
downloadlink="""
<a href="%s" >%s</a> </br>
"""

def geneProcess(resultdir, anaName, libname):
  import tuil
  from multiprocessing import Process
  countfile = os.path.join(resultdir, anaName+".count.txt")
  sortfile = os.path.join(resultdir, anaName+".count.sort.txt")
  libfile = os.path.join(os.path.dirname(resultdir), libname)
  dbfile = os.path.join(resultdir, anaName+"db")
  rankfile = os.path.join(resultdir, anaName+".rank.txt")
  # parellel 
  ps = []
  p = Process(target = tuil.sortgenefile, args=(countfile, sortfile))
  p.start()
  ps.append(p)
  p = Process(target = tuil.generaterankfile,args = (dbfile, countfile,
                                                     libfile, rankfile))
  p.start()
  ps.append(p)
  for p in ps:
    p.join()

def showdownloadfile(dir, file):
    dir = os.path.join("../", dir)
    print(downloadlink % ( os.path.join(dir, file), file))

def getvalue(inputkey):
  value = None
  if inputkey in form:
    value = form[inputkey].value
  return value

def main():
  anaName = getvalue(inputAnakey)
  libname = getvalue(inputLibrarykey)
  print(html % anaName)
  projectdir = os.path.join(uploaddir, anaName)
  resultdir = os.path.join(projectdir, "RESULT")
  if libname:
    geneProcess(resultdir, anaName, libname)

  for file in os.listdir(resultdir):
    showdownloadfile(resultdir, file)

main()






