#!/usr/bin/env python
import os, sys

if len(sys.argv) != 2:
  print("usage: %s directory" % sys.argv[0])
  os._exit(1)

directory = sys.argv[1]
files = os.listdir(directory)
for f in files:
  filesource = os.path.join(directory, f)
  filetarget = os.path.join(directory, f.replace(" ", "_"))
  os.rename(filesource, filetarget)

