#!/usr/bin/env python


import cgi, os,  sys
from subprocess import Popen, PIPE

debugmode = False
uploaddir = "./uploads"
sys.stderr = sys.stdout

if debugmode:
  class dummy:
    def __init__(self,s): self.value = s
  form = {'AnaName':dummy('test'),
          'fileR1':dummy('NGS-CRISPR_S9_L099_R1_001.clean.fastq.gz'),
          'fileR2':dummy('NGS-CRISPR_S9_L099_R2_001.clean.fastq.gz'),
          'library':dummy('Mageck.csv'),
          'label1':dummy('MyLable1'),
          'label2':dummy('MyLabel2')
  }
else:
  form = cgi.FieldStorage()

print("Content-type: text/html\n")
html = """
<h1>Analysis.page</h1>
<h2>Analysis command<h2>
<p>%s</p>
<!-- Download message -->
%s
<h2>Running message</h2>
<h6>%s</h6>
"""

downloadhtml= """
<h2>Download page</h2>
<form method=get action='downloadlist.py'>
<input type=hidden name=%s value="%s"> <!-- Anaylysis -->
<input type=hidden name=%s value="%s"> <!-- lib -->
<input type=submit value=downloadPage>
</form>
"""


def runprocess(cmd):
#  print("Run porcess ...")
  p = Popen(cmd, stdout = PIPE, stderr = PIPE ,shell=True)
  myOut, myErr = p.communicate()
  return myOut, myErr

def preparedata(anaName):
  workingdir = os.path.join(uploaddir, anaName)
  os.chdir(workingdir)
  os.system('cp ../../scripts/%s .' % scriptname)


from common import *
scriptname = 'runmageck.sh'
donefile = 'workdone'

def main():
  # process 
  inputkeytuple = (inputAnakey, inputR1key, inputR2key, inputLibrarykey,
                   inputLabel1key, inputLabel2key)
  (anaName, r1name, r2name, libname, label1, label2) = tuple(map(lambda x:
                                                                 form[x].value,
                                                                inputkeytuple))
  cmd = './%s ./%s %s ./%s %s ./%s %s' % (scriptname, libname, label1, r1name,
                                        label2, r2name, anaName)
  preparedata(anaName)
  myErr, myOut = "", ""
  if not os.path.exists("./" + donefile):
    myOut, myErr = runprocess(cmd)

  if os.path.exists(r"./" + donefile):
    print(html % (cgi.escape(cmd), downloadhtml % (inputAnakey, anaName, inputLibrarykey, libname), myErr + myOut) )
  else: # Error
    print(html % (cgi.escape(cmd), " ", myErr + myOut)) # sterror
 # print(html % ("stderror is ", myErr.decode().replace("\n", "<br>"))) # sterror

try:
  main()
except:
  print(sys.exc_info())

