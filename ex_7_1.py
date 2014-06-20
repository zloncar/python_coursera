# fname = raw_input("Filename: ")
fname = 'mbox-short.txt'

try:
  fh = open(fname)
except:
  print 'File cannot be opened:', fname
  exit()

count = 0
total_confidence = 0
for i in fh:
  if i.startswith('X-DSPAM-Confide'):
    i = i.rstrip()
    atpos = i.find(':')
    count = count + 1
    total_confidence = total_confidence + float(i[atpos+2:])
    print 'count:', count, ', confidence:', float(i[atpos+2:]), ', total_confidence:', total_confidence

average_confidence = total_confidence / count
print average_confidence
