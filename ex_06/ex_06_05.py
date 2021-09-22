str = 'X-DSPAM-Confidence:0.8475'
index = str.find(":")
print(index)
print(float(str[index + 1:]))