str = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
start_at = str.find('@') + 1
end_at = str.find(' ', start_at)
print str[start_at:end_at]

print 'decimal:%g, int:%d, string:%s.' % (3.1412, 3, 'three')

