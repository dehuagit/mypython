"read number till eof and show squares"

def interact():
  print('Hello stream world')
  while True:
    try:
      reply = input('Enter a nuber>')
    except EOFError:
      break
    else:
      num = int(reply)
      print("%d squard is %d" % (num, num ** 2))
  print('bye')

if __name__ == '__main__':
  interact()


