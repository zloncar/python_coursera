hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate per Hour: ")

try:
    hrs = float(hrs)
    rate = float(rate)

    if hrs > 40:
        extra_hrs = hrs-40
        pay = (40 * rate) + (extra_hrs * rate * 1.5)
    else:
        pay = hrs * rate

    print "Pay: ", pay

except:
    print "Your input should be numeric."
