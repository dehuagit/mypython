

def summer(numCols, fileName):
  sums = [0] * numCols
  for line in open(fileName):
    cols = line.split()
    nums = [int(x) for x in cols]
    both = zip(sums, nums)
    sums = [x + y for (x, y) in both]
  return sums


if __name__ == '__main__':
  import sys
  print(summer(eval(sys.argv[1]), sys.argv[2]))

