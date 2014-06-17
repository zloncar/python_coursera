arr = [2,-5.3, -3, 7, 1, 1, 1]

min = arr[0]
max = arr[0]

for i in arr:
  if i < min:
    min = i
  if i > max:
    max = i

print min
print max
