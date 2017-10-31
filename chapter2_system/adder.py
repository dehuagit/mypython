import sys

sum = 0
while True:
  try:
    line = input()  # or call sys.stdin.readlines()
  except EOFError:  # or for line in sys.stdion:
    break
  else:
    sum += int(line)
print(sum)

