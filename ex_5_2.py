min = None
max = None

while True:
  inp = raw_input('> ')

  if inp == 'd':
    break

  try:
    inp = float(inp)

    if max is None or inp > max:
      max = inp
    if min is None or inp < min:
      min = inp

  except:
    print "Your input should be numeric."

print 'min:', min
print 'max:', max
