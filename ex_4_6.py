hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate per Hour: ")

def computepay(hours, rate):
  if hours > 40:
    extra_hrs = hours-40
    pay = (40 * rate) + (extra_hrs * rate * 1.5)
  else:
    pay = hours * rate

  return pay

try:
  hrs = float(hrs)
  rate = float(rate)
  print computepay(hrs, rate)

except:
  print "Your input should be numeric."
