# fname = raw_input("Filename: ")
fname = 'mbox-short.txt'

try:
  fh = open(fname)
except:
  print 'File cannot be opened:', fname
  exit()

count = 0
for line in fh:
  if line.startswith('From: '):
    email = line.split()[1]
    count += 1
    print email
print "There were", count, "lines in the file with From as the first word"
