# Test = (1, 2, 3, 4, 5)
# print Test[0]
# print Test[1]

x = 10073
divisors = ()
for i in range(1,x):
  if x%i == 0:
    divisors = divisors+(i,)

print divisors
