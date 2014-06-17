i = 0
total = 0.0

while True:
  inp = raw_input('> ')
  if inp == 'd':
    break

  try:
    inp = float(inp)
    i = i + 1
    total = total + inp

  except:
    print "Your input should be numeric."

print i
print total

if i != 0:
  print total / i;
