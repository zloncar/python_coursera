word = raw_input("Word: ")
letter = raw_input("Letter: ")

def count(word, letter):
  k = 0

  for i in word:
    if i == letter:
      k = k + 1

  return k

if len(letter) != 1:
  print "Letter should be of length 1"
else:
  print 'Occurences of', letter,':', count(word, letter)

