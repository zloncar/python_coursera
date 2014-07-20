str = 'X-DSPAM-Confidence: 0.8475'

i = str.find(':') + 2
print float(str[i:])
