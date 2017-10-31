""
""

def more(text, numlines=10):
  lines = text.splitlines()
  while lines:
    chunk = lines[:numlines]  # 0 to 10 contain
    lines = lines[numlines:]  # oresst
    for line in chunk: print(line)
    if lines and input('More?') not in ['y', 'Y']: break


if __name__ == '__main__':
  import sys
  if len(sys.argv) == 1:        # page no cmd
    more(sys.stdin.read())
  else:
    more(open(sys.argv[1]).read())




