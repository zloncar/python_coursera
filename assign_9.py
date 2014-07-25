# fname = raw_input("Filename: ")
fname = 'mbox-short.txt'

try:
  fh = open(fname)
except:
  print 'File cannot be opened:', fname
  exit()

counts = dict()

for line in fh:
  if line.startswith('From '):
    email = line.split()[1]
    counts[email] = counts.get(email,0) + 1

count = None
email = None

for key, value in counts.items():
  if count is None or value > count:
    email = key
    count = value
print email, count

