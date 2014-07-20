# fname = raw_input("Filename: ")
fname = 'romeo.txt'

try:
  fh = open(fname)
except:
  print 'File cannot be opened:', fname
  exit()

arr = list()
for line in fh:
  words = line.rstrip().split()
  for word in words:
    if word in arr:
      continue
    else:
      arr.append(word)
arr.sort()
print arr
