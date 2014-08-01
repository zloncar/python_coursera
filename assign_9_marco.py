name = raw_input("Enter file:")
hd = open(name)
people = []
for line in hd:
    if line.startswith("From "):
        line_spl = line.split()
        sender = line_spl[1]
        people.append(sender)

amount = dict()
for person in people:
    amount[person] = amount.get(person,0) + 1

count = None
f_person = None
for key,value in amount.items():
    if count is None or value > count:
        f_person = key
        count = value
        
print f_person, count
