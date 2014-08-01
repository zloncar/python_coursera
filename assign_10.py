fname = 'mbox-short.txt'

try:
  fh = open(fname)
except:
  print 'File cannot be opened:', fname
  exit()

counts = dict()

for line in fh:
  if line.startswith('From '):
  	line = line.strip()
  	words = line.split()
  	hour = words[5].split(':')[0]
  	counts[hour] = counts.get(hour,0) + 1

lst = list()

for key, value in counts.items():
	lst.append( (key, value) )

lst.sort()

for key, value in lst:
	print key, value