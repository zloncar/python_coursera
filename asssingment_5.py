largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done":
        break
    elif num > largest:
        largest = num
    elif  num < smallest:
        smallest = num
    else:
        smallest = num
    try:
        num = int(num)
    except:
        print "Invalid input"
        continue

print "Maximum is", largest
print "Minimum is", smallest