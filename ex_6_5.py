str = 'X-DSPAM-Confidence: 0.8475'

i = str.find(':') + 2
print type(float(str[i]))
