#name = raw_input("Enter the file name:")
name = 'mbox-short.txt'
handle = open(name)

count = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time[:2]
        count[hour] = count.get(hour, 0) + 1

tup = count.items()
tup.sort()

for k, v in tup:
    print k, v